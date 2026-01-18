from django.urls import path

from . import views

app_name = "verificador"

urlpatterns = [
    path("hola/", views.hola, name="hola"),
    path("", views.home, name="home"),
]
