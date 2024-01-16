from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    response = render(request, "home.html")
    response.set_cookie("name", "sumon", expires=datetime.utcnow()+timedelta(days=15))
    response.set_cookie("name", "manu", max_age=10)
    return response

def get_cookie(request):
    name =request.COOKIES.get("name")
    return render(request, "getcookie.html", {"name":name})

def del_cookie(request):
    response = render(request, "delete.html")
    response.delete_cookie("name")
    return response

# session

def set_session(request):
    data = {
        "name":"sumon",
        "age": 25,
        "language": "python"
    }
    request.session.update(data)
    return render(request, "home.html")

def get_session(request):
    name = request.session.get("name")
    age = request.session.get("age")
    return render(request, "getcookie.html", {"name":name, "age":age})


def delete_session(request):
    # del request.session["name"]               # specific data delete
    request.session.flush()
    return render(request, "")