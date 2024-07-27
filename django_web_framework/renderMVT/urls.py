from django.urls import path
from renderMVT import views

urlpatterns = [
    path("time/", views.ShowTime, name="time"),
    path("list/", views.ShowValues, name="list"),
    path("response/", views.load_user, name="response"),
]