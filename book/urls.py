from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeTemplate.as_view(), name='home'),
    path("book-session/", views.BookTemplate.as_view(), name='book-session'),
    path("manage-session/", views.get_session, name='manage-session'),
]
