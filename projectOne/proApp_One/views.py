from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is proApp_One page.")

def courses(request):
    return HttpResponse("this is the couse page for application.")

def about(request):
    return HttpResponse("this is about page for application.")