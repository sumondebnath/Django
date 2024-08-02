from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Ebook(models.Model):
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    

class Review(models.Model):
    # review_author = models.CharField(max_length=10, null=True, blank=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return str(self.rating)