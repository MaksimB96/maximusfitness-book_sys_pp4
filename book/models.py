# imports

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Time slots for booking
SLOT = {
    ("8 AM", "8 AM"),
    ("10 AM", "10 AM"),
    ("12 PM", "12 PM"),
    ("2 PM", "2 PM"),
    ("4 PM", "4 PM"),
    ("6 PM", "6 PM"),
    ("8 PM", "8 PM"),
}


class SessionBook(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    booked_slot = models.CharField(max_length=10, choices=SLOT, default='8 AM')
    client_notes = models.TextField(blank=True)
    sent_on = models.DateField(default=datetime.now)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_on']

    def __str__(self):
        return self.user

