from django.db import models
from content.constants import CONTENT_TYPE

# Create your models here.

class Creator(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Content(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE, default=None)

    creator = models.ForeignKey(Creator, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name