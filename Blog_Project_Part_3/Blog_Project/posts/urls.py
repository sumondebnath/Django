from django.urls import path
from posts.views import add_post, edit_post, delete_post, addPostClassView, EditPostView, DeletePostView, detailsView

urlpatterns = [
    # path("add/", add_post, name="add_posts"),
    # path("edit/<int:id>", edit_post, name="edit_posts"),
    # path("delete/<int:id>", delete_post, name="delete_posts"),
    #class based views
    path("add/", addPostClassView.as_view(), name="add_posts"),
    path("edit/<int:id>/", EditPostView.as_view(), name="edit_posts"),
    path("delete/<int:id>", DeletePostView.as_view(), name="delete_posts"),
    path("details/<int:id>", detailsView.as_view(), name="details_posts"),
]