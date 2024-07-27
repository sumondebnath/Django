from django.urls import path
from bulk_concept import views


urlpatterns = [
    path("insert/", views.Voulentear_Bulk_insert, name="bulk_insert"),
]