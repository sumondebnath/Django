from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from profile_api.models import Profile, ProfileStatus
from profile_api.serializers import ProfileSerializer, ProfileStatusSerializer, AvaterSerializer
from profile_api.permissions import IsOwnProfileOrReadOnly, IsOwnOrReadOnly

# Create your views here.


class Profile_List(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]



class ProfileCombinedViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]




class ProfileStatusViewSets(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)




class AvaterUpdateViewset(generics.UpdateAPIView):
    serializer_class = AvaterSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object