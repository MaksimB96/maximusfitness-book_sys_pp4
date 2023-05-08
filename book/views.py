from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import CreateBooking


class HomeTemplate(TemplateView):
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
        return HttpResponseRedirect('home')


class BookTemplate(TemplateView):
    template_name = "book-session.html"

