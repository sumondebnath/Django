from django.urls import path
from authors.views import register, Login, Profile, ChangePassword, editProfile, LogOut, UserLogIn, UserLogOut

urlpatterns = [
    path("register/", register, name="register"),
    # path("login/", Login, name="log_in"),
    path("login/", UserLogIn.as_view(), name="log_in"),
    path("profile/", Profile, name="profile"),
    path("edit/profile/", editProfile, name="edit_profile"),
    path("edit/profile/password/change/", ChangePassword, name="change_pass"),
    # path("logout/", LogOut, name="log_out"),
    path("logout/", UserLogOut.as_view(), name="log_out"),
]