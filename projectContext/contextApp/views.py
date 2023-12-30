from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    cntx ={"name":"Sumon", "age":25, "list":[2, 1, 5, 3], "lst":[
        {
            "name" : "Sumon Debnath",
            "age" : 25,
            "gender" : "male"
        },
        {
            "name" : "Manu Debnath",
            "age" : 24,
            "gender" : "men"
        },
        {
            "name" : "unknown",
            "age" : "undefined",
            "gender" : "unknown"
        }
    ], 
    "lst1" : ["My", "Name", "is", "Sumon"], "birthdate" : datetime.datetime.now(), "val": ["sumon deb nath manu", "only sumon"]}
    
    return render(request, "contextApp/home.html", context=cntx)     # without context we can pass the only cntx variable.