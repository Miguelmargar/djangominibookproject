from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=254, blank=False)
    author = models.CharField(max_length=254, blank=False)
    isbn = models.CharField(max_length=254, blank=False)
    notes = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')