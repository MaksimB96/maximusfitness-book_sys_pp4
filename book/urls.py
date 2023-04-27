from django.urls import path


urlpatterns = [
    path("", include('book.urls'))
]
