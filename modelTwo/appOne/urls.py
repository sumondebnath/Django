from django.urls import path
from appOne.views import home

urlpatterns = [
    path("", home, name="home")
]