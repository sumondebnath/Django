from django.urls import path
from validation_concept import views


urlpatterns = [
    path("registration/", views.UserRegistrationView, name="registration"),
]