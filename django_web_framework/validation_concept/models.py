from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here. uncomment used to validated by custom developer.

class UserRegistration(models.Model):
    # username = models.CharField(max_length=30, verbose_name="Username")
    username = models.CharField(max_length=30, verbose_name="Username", validators=[MaxLengthValidator(10)])

    # first_name = models.CharField(max_length=30, verbose_name="First Name")
    first_name = models.CharField(max_length=30, verbose_name="First Name", validators=[MinLengthValidator(4)])

    # last_name = models.CharField(max_length=30, verbose_name="Last Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name", validators=[MinLengthValidator(4)])

    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=14, verbose_name="Phone Number")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=20, verbose_name="Gender")
    website_url = models.URLField(verbose_name="Webite URL")

    # password = models.CharField(max_length=15, verbose_name="Password") 
    password = models.CharField(max_length=15, verbose_name="Password", validators=[MinLengthValidator(5)])

    # confirm_password = models.CharField(max_length=15, verbose_name="Confirm Password")
    confirm_password = models.CharField(max_length=15, verbose_name="Confirm Password", validators=[MinLengthValidator(5)])