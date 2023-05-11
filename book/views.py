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
def book_session(request):
    """
    Allows User to book a session via form from forms.py
    """
    if request.method == 'POST':
        booking = SessionBook(user=request.user)
        form = CreateBooking(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('manage-session')
    else:
        form = CreateBooking()
    return render(request, 'book-session.html', {
        'form': form})


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
def update_session(request, id):
    """
    Provides Functionality for Updating existing booking
    """
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


@login_required
def delete_session(request, id):
    """
    Provides functionality for deletion of items 
    """
    session = get_object_or_404(CreateBooking, pk=id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('manage_session')
    return render(request, 'delete-session.html', {
        'session': session
    })