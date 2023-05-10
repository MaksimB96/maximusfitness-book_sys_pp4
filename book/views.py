from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.views import generic, View
from django.core.mail import send_mail
from django.conf import settings
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
    if request.method == 'POST':
        form = CreateBooking(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage-session')
    form = CreateBooking()
    context = {
        'form': form
    }
    return render(request, 'book-session.html', context)


@login_required
def get_session(request):
    item = SessionBook.objects.all()
    context = {
        'item': item
    }
    return render(request, 'manage-session.html', context)


@login_required
def update_session(request, id):
    if request.method == 'POST':
        session = get_object_or_404(CreateBooking, pk=id, user=request.user)
        form = UpdateBooking(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage-session')
        else:
            form = UpdateBooking()
            context = {
                'form': form,
            }
        return render(request, 'update-session.html', context)

