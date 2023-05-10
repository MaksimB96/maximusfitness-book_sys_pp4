from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic, View
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import SessionBook
from .forms import CreateBooking, UpdateBooking
from django.contrib.auth.decorators import login_required


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
        return HttpResponse('home')


@login_required
def get_session(request):
    """
    Gets User bookings
    """
    user = request.user
    items = SessionBook.objects.filter(user=user)
    return render(request, 'manage-session.html', {
        'user': user,
        'items': items,
    })


@login_required
def book_session(request):
    """
    Allows User to book a session via form from forms.py
    """
    if request.method == 'POST':
        booking = SessionBook(user=request.user)
        form = CreateBooking(request.POST, instance=booking)
        if form.is_valid():
            users_time = request.POST.get('time')
            users_date = request.POST.get('date')
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Booking Succesfully Created for:"
                f"{users_time} on {users_date}"
            )
            return redirect('manage-booking')
        else:
            messages.add_message(
                request, messages.ERROR,
                "test Error"
            )
            url = reverse('account_login')
            return HttpResponseRedirect(url)
    else:
        form = CreateBooking()
    return render(request, 'book-session.html', {'form': form})


@login_required
def update_session(request, id):
    if request.method == 'POST':
        session = get_object_or_404(CreateBooking, pk=id, user=request.user)
        form = UpdateBooking(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('manage-session')
        else:
            form = UpdateBooking()
            context = {
                'form': form,
            }
        return render(request, 'update-session.html', context)
