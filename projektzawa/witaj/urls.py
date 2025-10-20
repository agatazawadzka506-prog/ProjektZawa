from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="home"),
    path("hello/", views.hello, name="hello"),
    path("hello/<str:name>/", views.hello_name, name="hello_name"),
    path("hello_template/<str:name>/", views.hello_template, name="hello_template"),
]

