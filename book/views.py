from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.views import generic, View
from django.core.mail import send_mail
from django.conf import settings
from .models import SessionBook


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


class BookTemplate(generic.CreateView):
    """
    Creates view to handle rendering booking form
    """
    template_name = "book-session.html"
    model = SessionBook

    fields = ['fname', 'lname', 'age', 'email',
              'phone', 'booked_slot', 'client_notes']

    success_url = "/manage-session"


def get_session(request):
    item = SessionBook.objects.all()
    context = {
        'item':item
    }
    return render(request, 'templates/manage-session.html', context)
