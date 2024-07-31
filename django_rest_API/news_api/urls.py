from django.urls import path
from news_api import views


urlpatterns = [
        #Function Based Views
    path("list/", views.article_list_api_view, name="article-list"),
    path("list/<int:pk>/", views.article_details_api_view, name="article-details"),

        # Class Based Views
    path("article/", views.ArticleListCreateAPIView.as_view(), name="articles"),
    path("article/<int:pk>/", views.ArticleDetailsAPIView.as_view(), name="articles_details"),

    path("journalist/", views.JournalistListCreateAPIView.as_view(), name="jornalists"),
    # path("journalist/<int:pk>/", views.JournalistDetailsAPIView.as_view(), name="jornalists_details"),
]