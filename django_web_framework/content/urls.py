from django.urls import path
from content import views

urlpatterns = [
    path("all_content/", views.AllContent, name="all_content"),
    path("content_list/", views.ContentList, name="content_list"),

    path("get_details/<int:id>", views.getContent, name="get_details"),
    path("get_content_foreign/<int:id>", views.getContentForeign, name="get_content_foreign"),

    path("delete_content/<int:id>", views.deleteContent, name="delete_content"),

    path("edit_content/<int:id>", views.EditContent, name="edit_content"),
    path("edit_content_foreign/<int:id>", views.EditContentForeign, name="edit_content_foreign"),

    path("insert_content/", views.insertContent, name="insert_content"),

    path("pagination/", views.Content_Pagination, name="pagination"),
]