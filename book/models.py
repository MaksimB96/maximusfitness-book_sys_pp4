# imports

from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


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
    time = models.TimeField("Pick a Time")
    client_notes = models.TextField("Leave Your Request Here", blank=True)
    sent_on = models.DateField(default=datetime.now)
    update_on = models.DateTimeField(auto_now=True, blank=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_on']

    def __str__(self):
        return f"{self.fname} | {self.date} | {self.time}"
