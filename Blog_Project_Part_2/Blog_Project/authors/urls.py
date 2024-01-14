from django.urls import path
from authors.views import register, Login, Profile, ChangePassword, editProfile, LogOut

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", Login, name="log_in"),
    path("profile/", Profile, name="profile"),
    path("edit/profile/", editProfile, name="edit_profile"),
    path("edit/profile/password/change/", ChangePassword, name="change_pass"),
    path("logout/", LogOut, name="log_out"),
]