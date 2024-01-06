from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("form/", views.submitForm, name="form"),
    path("djangoForm/", views.djangoForm, name = "djangoForm"),
    path("login/", views.Login, name="login"),
    path("password/", views.passwordvalidation, name="password"),
]