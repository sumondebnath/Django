from django.shortcuts import render
from django.http import JsonResponse
from first_api.models import Manufacturer, Product

# Create your views here.

def Product_List(request):
    products = Product.objects.all()
    data = {
        "products" : list(products.values()),
        # "products" : list(products.values("pk", "name"))
    }
    response = JsonResponse(data)
    return response


def Product_Details(request, pk):
    try:
        product = Product.objects.get(pk = pk)
        data = {
            "product":{
                "name" : product.name,
                "manufacturer" : product.manufacturer.name,
                "photo" : product.photo.url,
                "price" : product.price,
                "quantity" : product.quantity,
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code" : 404,
                "message" : "Product Not Found!",
            }
        }, status = 404)
    return response


def Manufacturer_list(request):
    # manufacturers = Manufacturer.objects.all()
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {
        "manufacturers" : list(manufacturers.values()),
    }
    response = JsonResponse(data)
    return response


def Manufacturer_Details(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {
            "manufacturer" : {
                "name" : manufacturer.name,
                "location" : manufacturer.location,
                "active" : manufacturer.active,
                "products" : list(manufacturer_products.values()),
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error" : {
                "code" : 404,
                "message" : "Manufacturer Not Founded!",
            }
        }, status = 404)
    
    return response



# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# class ManufacturerDetailsView(DetailView):
#     model = Manufacturer
#     template_name = ""


# class ProductListView(ListView):
#     model = Product
#     template_name = "" 