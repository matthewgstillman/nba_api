from __future__ import unicode_literals
from forms import MovieForm
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class MovieManager(models.Manager):
    def login(self):
        return self

    def add_movie(self, postData):
        title = request.POST['title']
        year = request.POST['year']
        genre = request.POST['genre']
        director = request.POST['director']
        lead_role_1 = request.POST['lead_role_1']
        lead_role_2 = request.POST['lead_role_2']
        rating = request.POST['rating']
        review = request.POST['review']
        Movie.objects.create(title=title, year=year, genre=genre, director=director, lead_role_1=lead_role_1, lead_role_2=lead_role_2, rating=rating, review=review)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(choices=YEAR_CHOICES)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    director = models.CharField(max_length=50)
    lead_role_1 = models.CharField(max_length=50)
    lead_role_2 = models.CharField(max_length=50)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField(max_length=1500)
    # reviewer = models.ForeignKey('User', related_name="user_reviewer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()

    def __unicode__(self):
        return "id: " + str(self.id) + ", Movie Title: " + str(self.title) + ", Year: " + str(self.year) +  ", Genre: " + str(self.genre) + ", Director: " + str(self.director) + ", Lead Role: " + str(self.lead_role_1) + ", Second Lead Role: " + str(self.lead_role_2) + ", Rating: " + str(self.rating) + ", Review: " + str(self.review)

class ShitManager(models.Manager):
    def login(self):
        return self

