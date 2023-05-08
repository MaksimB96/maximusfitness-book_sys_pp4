from .models import SessionBook
from django.forms import ModelForm
from django import forms


class CreateBooking(forms.ModelForm):
    class Meta:
        model = SessionBook
        fields = ('fname', 'lname', 'age', 'email',
                  'phone', 'date_booked', 'client_notes',)
