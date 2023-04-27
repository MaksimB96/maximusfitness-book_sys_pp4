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


class Booking(models.Model):
    """
    booking class utilizes user/ day/ time and confirmation status above
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service = models.CharField(max_length = 50,
     choices=SERVICES_CHOICE, default='One on One'
     )
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10,
     choices=BOOKING_SLOT, default='8 AM'
     )
    confirm_status = models.CharField(max_length=10,
     choices=CONFIRMATION_STATUS, default='pending'
     )

    class Meta:
        ordering = ['day']

    def __str__(self):
        return f'User: {self.user} | Date: {self.day} | Time: {self.time} | Status: {self.confirm_status}'
