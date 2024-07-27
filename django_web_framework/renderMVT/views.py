from django.shortcuts import render
import datetime

import requests

# Create your views here.

def ShowTime(request):
    todayDate = datetime.datetime.now()
    return render(request, "renderMVT/showTime.html", {"date": todayDate})


def ShowValues(request):
    nameList = ["aaa", "bbb", "ccc", "ddd", "eee", "ffff", "ggg", 'hhhh', 'iiii', "jjj", "kkk"]
    template_name = "renderMVT/example.html"
    return render(request, template_name, {"lists":nameList})



def callRestAPI():
    Base_url = "https://fakestoreapi.com"
    response = requests.get(f'{Base_url}/users')
    return response.json()

def load_user(request):
    response = callRestAPI()
    return render(request, "renderMVT/fakeAPI.html", {"responses" : response})