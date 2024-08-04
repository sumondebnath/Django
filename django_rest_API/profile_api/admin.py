from django.contrib import admin
from profile_api.models import Profile, ProfileStatus

# Register your models here.

admin.site.register(Profile)
admin.site.register(ProfileStatus)