from django.db import models
from django.urls import reverse

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    director = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'movie_id': self.id})
    
    