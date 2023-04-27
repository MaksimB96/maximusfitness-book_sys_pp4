from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class PostBooking(SummernoteModelAdmin):

    list_filter = ('confirm_status', )
