from django.shortcuts import render, redirect
from authors.forms import authorForm

# Create your views here.
def add_author(request):
    if request.method == "POST":
        form = authorForm(request.POST)
        if form.is_valid():
            # print(request.POST)
            form.save()
            return redirect("add_authors")
    else:
        form = authorForm()
    return render(request, "authors/add_author.html", {"form":form})