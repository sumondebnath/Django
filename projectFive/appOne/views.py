from django.shortcuts import render
from .forms import contactForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("userName")
        email = request.POST.get("email")
        select = request.POST.get("select")
        return render(request, "about.html", {"name":name, "email":email, "select":select})
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

def djangoForm(request):
    if request.method == "POST":
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            with open("./appOne/upload/" + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, "djangoForms.html", {"form":form})
    else:
        form = contactForm()
    return render(request, "djangoForms.html", {"form":form})