from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeTemplate.as_view(), name='home'),
    path("book-session/", views.book_session, name='book-session'),
    path("manage-session/", views.get_session, name='manage-session'),
    path("update-session/<id>", views.update_session, name='update-session'),
]
