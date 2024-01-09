from django.urls import path
from posts.views import add_post, edit_post, delete_post

urlpatterns = [
    path("add/", add_post, name="add_posts"),
    path("edit/<int:id>", edit_post, name="edit_posts"),
    path("delete/<int:id>", delete_post, name="delete_posts"),
]