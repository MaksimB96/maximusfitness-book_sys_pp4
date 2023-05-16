from .models import SessionBook
from django.forms import ModelForm
from django.utils import timezone
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'text'


class CreateBooking(forms.ModelForm):
    class Meta:
        model = SessionBook
        fields = ('fname', 'lname', 'email', 'phone',
                  'age', 'date', 'time', 'client_notes',)
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Select a Date',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(attrs={
                'type': 'time'}
                ),

        }

    def clean_date(self):
        data = self.cleaned_data['date']
        if data < timezone.now().date():
            raise forms.ValidationError("You Can't book a date already past!")
        return data


class UpdateBooking(forms.ModelForm):
    class Meta:
        model = SessionBook
        fields = ('date', 'time',)
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Select a Date',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(attrs={
                'type': 'time'}
                ),
        }
