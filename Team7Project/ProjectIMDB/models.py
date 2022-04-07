from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Genre(models.Model):
    genre_title = models.CharField(max_length=20)

    def __str__(self):
        return self.genre_title


class Actor(models.Model):
    full_name = models.CharField(max_length=80)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.full_name


class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    ]
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=5)
    review = models.TextField(max_length=2000, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    release_year = models.CharField(max_length=25, blank=True)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    director = models.CharField(max_length=100, blank=False)
    writer = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=900, blank=True)
    rating = models.ManyToManyField(Rating)
    picture = models.ImageField(upload_to="upload/", blank=True)

    def __str__(self):
        return self.movie_title



