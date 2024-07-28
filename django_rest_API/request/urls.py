from django.urls import path

from request import views


urlpatterns = [
    path("get_request/", views.main, name="get_request"),
]