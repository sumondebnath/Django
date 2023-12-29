from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def lastHome(request):
    return HttpResponse("this is last home page.")

def last(request):
    return HttpResponse("this is last page.")