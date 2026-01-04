from django.urls import path

from . import views

app_name = 'atelier'

urlpatterns = [
    path("", views.index, name="index"),
]