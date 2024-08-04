"""
URL configuration for django_rest_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("rest_framework.urls")),      # this is for the log-in / out option created in rest_framework page.
    # path("api/rest-auth/", include("rest_auth.urls")),      # this is the rest_auth authentication provide by django_rest_auth package but its given error
    path("api/rest-auth/", include("dj_rest_auth.urls")),      # thats why using the dj_rest_auth, it is similar django_rest_auth

    # path("", include("request.urls")),
    path("api/", include("first_api.urls")),
    path("api/articles/", include("news_api.urls")),

    path("ebooks/", include("ebook_api.urls")),

    path("profile_api/", include("profile_api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)