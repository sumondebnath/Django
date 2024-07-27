# Generated by Django 4.2.13 on 2024-07-23 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation_concept', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='confirm_password',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Confirm Password'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(10)], verbose_name='Username'),
        ),
    ]
