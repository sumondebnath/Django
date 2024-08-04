
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api.views import Profile_List, ProfileViewSet, ProfileCombinedViewSet, ProfileStatusViewSets, AvaterUpdateViewset


profile_list_viewset = ProfileViewSet.as_view({
    "get" : "list",
})
profile_details_viewset = ProfileViewSet.as_view({
    "get" : "retrieve",
})



router = DefaultRouter()
router.register(r"profile_router", ProfileViewSet)
router.register(r"profile_permission", ProfileCombinedViewSet, basename="profile_permission")
router.register(r"profile_status", ProfileStatusViewSets, basename="profile_status")




urlpatterns = [
    path("profiles/", Profile_List.as_view(), name="profilelist"),

    path("profiles_list/", profile_list_viewset, name="profile_list"),
    path("profiles_list/<int:pk>/", profile_details_viewset, name="profile_list"),

    path("", include(router.urls)),

    path("avater/", AvaterUpdateViewset.as_view(), name="avater"),
]