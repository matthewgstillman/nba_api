from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()

    def __unicode__(self):
      return "id: " + str(self.id) + ", First Name: " + str(self.first_name) + ", First Name: " + str(self.first_name) + ", Last Name: " + str(self.last_name) + ", Username: " + str(self.username) + ", email: " + self.email


