from django.db import models

# Create your models here.

class Voulentears(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    professions = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.professions}"