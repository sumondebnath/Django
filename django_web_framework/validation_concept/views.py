from django.shortcuts import render, redirect
from validation_concept.forms import UserRegistrationForm

# Create your views here.

def UserRegistrationView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect("registration")
    else:
        form = UserRegistrationForm()
    return render(request, "validation_concept/userRegistration.html", {"form":form})