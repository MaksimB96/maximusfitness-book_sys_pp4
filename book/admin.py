from django.contrib import admin
from .models import SessionBook
from django_summernote.admin import SummernoteModelAdmin


@admin.register(SessionBook)
class AdminSession(SummernoteModelAdmin):
    list_filter = ('confirmed', 'sent_on')
    summernote_fields = ('client_notes')
