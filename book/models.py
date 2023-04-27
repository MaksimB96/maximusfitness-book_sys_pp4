# imports

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Time slots for booking
BOOKING_SLOT = {
    ("8 AM", "8 AM"),
    ("10 AM", "10 AM"),
    ("12 PM", "12 PM"),
    ("2 PM", "2 PM"),
    ("4 PM", "4 PM"),
    ("6 PM", "6 PM"),
    ("8 PM", "8 PM"),
}


SERVICES_CHOICE = {
    ("One on One", "One on One"),
    ("Consultation", "Consultation"),
    ("PT Package", "PT Package"),
}


# Confirmation Status of booking
CONFIRMATION_STATUS = {
    ("confirmed", "confirmed"),
    ("declined", "declined"),
    ("pending", "pending"),
}


