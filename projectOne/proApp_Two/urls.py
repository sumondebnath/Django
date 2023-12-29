
from django.urls import path
from .import views

urlpatterns = [
    path("", views.lastHome),
    path("last/", views.last),
]