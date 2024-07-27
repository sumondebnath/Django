from django.shortcuts import render
from django.http import HttpResponse
# from requests import request

# Create your views here.

def Test(request):
    return HttpResponse("This is for the Test Perpose!")


def Get_Request(request):
    if request.method == "GET":
        if request.GET.get("message"):
            message = request.GET.get("message")
        else:
            message = " "

        if request.GET.get("number"):
            message += request.GET.get("number")
        else:
            message = " "

    return HttpResponse(message)