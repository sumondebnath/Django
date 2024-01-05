from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    if request.method == "POST":
        name = request.POST.get("userName")
        email = request.POST.get("email")
        return render(request, "about.html", {"name":name, "email":email})
    else:
        return render(request, "about.html")

def submitForm(request):
    # print(request.POST)
    # if request.method == "POST":
    #     name = request.POST.get("userName")
    #     email = request.POST.get("email")
    #     return render(request, "form.html", {"name":name, "email":email})
    # else:
    #     return render(request, "form.html")
    return render(request, "form.html")