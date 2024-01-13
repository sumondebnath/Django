from django.shortcuts import render, redirect
from appOne.forms import RegisterForm, changeData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def home(request):
    return render(request, "appOne/home.html")

def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully!")
                # print(form.cleaned_data)
                return redirect("login")
        else:
            form = RegisterForm()
        return render(request, "appOne/signup.html", {"form":form})
    else:
        return redirect("profile")

def logIn(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data =request.POST)
            if form.is_valid():
                name = form.cleaned_data["username"]
                passwrd = form.cleaned_data["password"]
                user = authenticate(username=name, password=passwrd)
                if user is not None:
                    login(request, user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request, "appOne/login.html", {"form":form})
    else:
        return redirect("profile")


def profile(request):
    if request.user.is_authenticated:
        return render(request, "appOne/profile.html", {"user":request.user})
    else:
        return redirect("login")


def logOut(request):
    logout(request)
    return redirect("login")


def changePassword_usingOldPass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "appOne/changePassword.html", {"form":form})
    else:
        return redirect("login")


def changePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(request.user)
        return render(request, "appOne/changePassword.html", {"form":form})
    else:
        return redirect("login")
    

def updateData(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = changeData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Updated Successfully!")
                return redirect("profile")
        else:
            form = changeData(instance=request.user)
        return render(request, "appOne/updateData.html", {"form":form})
    else:
        return redirect("login")