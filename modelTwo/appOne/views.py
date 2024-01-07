from django.shortcuts import render
from appOne.forms import StudentForm

# Create your views here.
def home(request):
    # std = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, "appOne/home.html", {"form":form})