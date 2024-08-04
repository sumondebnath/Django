from rest_framework import serializers
from profile_api.models import Profile, ProfileStatus


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    avater = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class AvaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["avater", ]



class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"