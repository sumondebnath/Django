from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is app home.")

def test(request):
    return render(request, "appOne/home.html")
