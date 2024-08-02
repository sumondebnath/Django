# Generated by Django 4.2.13 on 2024-08-02 09:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_author', models.CharField(blank=True, max_length=10, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ebook_api.ebook')),
            ],
        ),
    ]