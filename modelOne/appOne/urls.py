from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delete/<int:roll>", views.delete, name="delete"),
]