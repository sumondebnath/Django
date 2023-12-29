
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is home page.")

def contact(request):
    return HttpResponse("this is the begining")

def doctor(request):
    return HttpResponse("Call the doctor right now.")