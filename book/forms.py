from .models import SessionBook
from django.forms import ModelForm
from django import forms


class CreateBooking(forms.ModelForm):
    class Meta:
        model = SessionBook
        fields = ('fname', 'lname', 'age', 'email',
                  'phone', 'date', 'client_notes',)
        date = forms.DateField(
            input_formats=['%d/%m/%Y'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        )
