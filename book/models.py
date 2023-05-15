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

    TIMESLOT_LIST = (
        (0, '09:00 - 09:30'),
        (1, '10:00 - 10:30'),
        (2, '11:00 - 11:30'),
        (3, '12:00 - 12:30'),
        (4, '13:00 - 13:30'),
        (5, '14:00 - 14:30'),
        (6, '15:00 - 15:30'),
        (7, '16:00 - 16:30'),
        (8, '17:00 - 17:30'),
    )

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
    time = models.IntegerField("Pick a Time", choices=TIMESLOT_LIST)
    client_notes = models.TextField("Leave Your Request Here", blank=True)
    sent_on = models.DateField(default=datetime.now)
    update_on = models.DateTimeField(auto_now=True, blank=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_on']

    def __str__(self):
        return f"{self.fname} | {self.date} | {self.time}"
