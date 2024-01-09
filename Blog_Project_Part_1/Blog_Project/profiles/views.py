from django.shortcuts import render, redirect
from profiles.forms import profileForm
# Create your views here.
def add_profile(request):
    if request.method == "POST":
        form = profileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_profiles")
    else:
        form = profileForm()
    return render(request, "profiles/add_profiles.html", {"form":form})