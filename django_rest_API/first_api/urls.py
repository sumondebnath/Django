from django.urls import path
from first_api.views import Product_List, Product_Details

urlpatterns = [
    path("products/", Product_List, name="product_list"),
    path("products/<int:pk>/", Product_Details, name="product_details"),
]