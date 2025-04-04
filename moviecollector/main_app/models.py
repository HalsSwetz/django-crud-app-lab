from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
SOURCES = (
    ('I', 'IMDB'),
    ('RT', 'Rotten Tomatoes'),
    ('M', 'Metacritic')
)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    director = models.CharField(max_length=100)
    year = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'movie_id': self.id})
    
class Critic(models.Model):
    source = models.CharField(
        max_length=50,
        choices=SOURCES,
        default=SOURCES[0][0]
    )
    rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
    ) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Rating from {self.get_source_display()}: {self.rating}'