from django.urls import path
from .import views

urlpatterns = [
    # path("", views.home),
    path("", views.set_session),
    # path("get/", views.get_cookie),
    path("get/", views.get_session),
    path("delete/", views.del_cookie),
]