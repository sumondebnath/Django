from django.urls import path
from appOne.views import home, signUp, logIn, profile, logOut, changePassword_usingOldPass, changePassword, updateData

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signUp, name="sign_up"),
    path("login/", logIn, name="login"),
    path("logout/", logOut, name="logout"),
    path("profile/", profile, name="profile"),
    path("change/password/usingOld/", changePassword_usingOldPass, name="change_Password_oldPassword"),
    path("change/password/", changePassword, name="change_password"),
    path("update/data/", updateData, name="update_data"),
]