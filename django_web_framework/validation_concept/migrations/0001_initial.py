# Generated by Django 4.2.13 on 2024-07-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Username')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(max_length=20, verbose_name='Gender')),
                ('website_url', models.URLField(verbose_name='Webite URL')),
                ('password', models.CharField(max_length=15, verbose_name='Password')),
                ('confirm_password', models.CharField(max_length=15, verbose_name='Confirm Password')),
            ],
        ),
    ]
