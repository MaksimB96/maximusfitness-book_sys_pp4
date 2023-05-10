from .models import SessionBook
from django.forms import ModelForm
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'text'


class CreateBooking(forms.ModelForm):
    class Meta:
        model = SessionBook
        fields = ('fname', 'lname', 'age', 'date', 'time', 'client_notes',)
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Select a Date',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),
        }