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
    ("6 PM", "6 PM"),
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
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=BOOKING_SLOT, default='8 AM')
    client_req = models.TextField()
    confirm_status = models.CharField(max_length=10, choices=CONFIRMATION_STATUS, default='pending')

    def __str__(self):
        return f'User: {self.user} Date: {self.day} Time: {self.time} Status: {self.confirm_status}'
