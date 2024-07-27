from django.urls import path
from request import views

urlpatterns = [
    path("test/", views.Test, name="test"),
    path("get_request/", views.Get_Request, name="get_request"),
        # get_request/?message=hello&number=10
    
]