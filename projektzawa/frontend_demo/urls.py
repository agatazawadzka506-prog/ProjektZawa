from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # tu podajesz tylko ścieżki dla aplikacji frontend_demo
]
