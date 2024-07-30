from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=120)
    photo = models.ImageField(null=True, default=True)
    price = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name