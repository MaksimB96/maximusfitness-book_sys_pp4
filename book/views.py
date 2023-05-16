from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic, View
from django.core.mail import send_mail
from django.conf import settings
from .models import SessionBook
from .forms import CreateBooking, UpdateBooking
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class HomeTemplate(generic.TemplateView):
    """
    This view handles rendering the home page and deals with sending emails
    via send_mail django functionality
    """
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        body = request.POST.get("contact-text")
        subject = f"{name} has a message for you!"

        send_mail(
            subject,
            body,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            [email],
        )
        home = reverse('home')
        # message.success implement here! (flash message)
        return HttpResponseRedirect(home)


@login_required
def book_session(request):
    """
    Allows User to book a session via form from forms.py
    """
    if request.method == 'POST':
        booking = SessionBook(user=request.user)
        form = CreateBooking(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Session has been booked!")
            return redirect('manage-session')   
        else:
            new_booking = form.save(commit=False)
            existing_booking = SessionBook.objects.filter(date=new_booking.date, time=new_booking.time)
            if existing_booking:
                messages.error(request, "Time slot already booked!")
                return redirect('book-session')
            else:
                form.save()    
    else:
        form = CreateBooking()
    return render(request, 'book-session.html', {
        'form': form
    })


@login_required
def get_session(request):
    """
    Gets User bookings
    """
    items = SessionBook.objects.filter(user=request.user)
    paginator = Paginator(items, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'manage-session.html', {
        'page_obj': page_obj,
    })


@login_required
def update_session(request, id):
    """
    Provides Functionality for Updating existing booking
    """
    form = UpdateBooking()
    if request.method == 'POST':
        session = get_object_or_404(SessionBook, pk=id, user=request.user)
        form = UpdateBooking(request.POST, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking Has Been Updated Successfully!")
            return redirect('manage-session')
    context = {
        'form': form,
    }
    return render(request, 'update-session.html', context)


@login_required
def delete_session(request, id):
    """
    Provides functionality for deletion of items
    """
    session = get_object_or_404(SessionBook, pk=id, user=request.user)
    if request.method == 'POST':
        session.delete()
        messages.success(request, "Session Deleted Successfully!")
        return redirect('manage-session')
    return render(request, 'delete-session.html', {
        'session': session,
    })
