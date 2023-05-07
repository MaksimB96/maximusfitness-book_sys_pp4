from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage


class HomeTemplate(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("contact_message")

        email = EmailMessage(
            subject=f"{name} wishes to get in contact with you!"
        )


class BookTemplate(TemplateView):
    template_name = "book-session.html"

    def post(self, request):
        name = request.POST.get()
        email = request.POST.get()
        message = request.POST.get()
