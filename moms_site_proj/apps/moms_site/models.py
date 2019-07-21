from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Email(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
