# imports

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Time slots for booking
BOOKING_SLOT = {
    ("8 AM", "8 AM"),
    ("10 AM", "10 AM"),
    ("12 AM", "12 AM"),
    ("2 AM", "2 AM"),
    ("4 AM", "4 AM"),
    ("6 AM", "6 AM"),
    ("6 AM", "6 AM"),
}


# Confirmation Status of booking
CONFIRMATION_STATUS = {
    ("confirmed", "confirmed"),
    ("declined", "declined"),
    ("pending", "pending"),
}
