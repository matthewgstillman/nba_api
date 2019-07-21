from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=40)
    dojo_location = models.CharField(max_length=2)
    favorite_language = models.TextField()
    comment = models.TextField(max_length=100)