# imports

from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
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
    """
    Model For booking a one on one session
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    fname = models.CharField("First Name", max_length=15, blank=True)
    lname = models.CharField("Last Name", max_length=15, blank=True)
    age = models.IntegerField(
        "Age",
        null=False,
        blank=False,
        default=18,
        validators=[
            MinValueValidator(18),
            MaxValueValidator(80)
        ]
    )
    email = models.EmailField("E-Mail", )
    phone = models.CharField("Phone No.", max_length=15)
    date = models.DateField("Pick a Date", default=datetime.now)
    time = models.CharField(
        "Pick a Slot", max_length=10, choices=SLOT, default='8 AM')
    client_notes = models.TextField("Leave Your Request Here", blank=True)
    sent_on = models.DateField(default=datetime.now)
    update_on = models.DateTimeField(auto_now=True, blank=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_on']

    def __str__(self):
        return self.fname
