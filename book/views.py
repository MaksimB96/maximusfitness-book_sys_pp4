from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings


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
        return HttpResponse('home')


class BookTemplate(TemplateView):
    template_name = "book-session.html"
