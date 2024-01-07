from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    student = models.Student.objects.all()
    # print(student)
    return render(request, "appOne/home.html", {"datas":student})

def delete(request, roll):
    std=models.Student.objects.get(pk = roll).delete()
    print(std)
    return redirect("home")