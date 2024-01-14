from django.shortcuts import render, redirect
from authors.forms import RegistrationForm, UserChangeData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # print(request.POST)
            form.save()
            messages.success(request, "Register Successfully!")
            return redirect("register")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form":form, "type":"Register"})


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            passwrd = form.cleaned_data["password"]
            user = authenticate(username=name, password=passwrd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged In Successfully!")
                return redirect("home")
            else:
                messages.warning(request, "Login Information Incorrect!")
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "register.html", {"form":form, "type":"Log In"})


@login_required
def Profile(request):
    # if request.method == "POST":
    #     form = UserChangeData(request.POST, instance=request.user)
    #     if form.is_valid():
    #         # print(request.POST)
    #         form.save()
    #         messages.success(request, "Register Successfully!")
    #         return redirect("profile")
    # else:
    #     form = UserChangeData(instance=request.user)

    data = Post.objects.filter(author=request.user)
    return render(request, "profile.html", {"data":data})


@login_required
def editProfile(request):
    if request.method == "POST":
        form = UserChangeData(request.POST, instance=request.user)
        if form.is_valid():
            # print(request.POST)
            form.save()
            messages.success(request, "Register Successfully!")
            return redirect("edit_profile")
    else:
        form = UserChangeData(instance=request.user)
    return render(request, "updateProfile.html", {"form":form})


def ChangePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Change Successfully")
            return redirect("profile")
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, "changePassword.html", {"form":form})

def LogOut(request):
    logout(request)
    return redirect("log_in")