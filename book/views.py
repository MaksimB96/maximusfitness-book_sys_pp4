from django.shortcuts import render, HttpResponse
from .models import Booking


def home(request):
    return HttpResponse("it's working")
