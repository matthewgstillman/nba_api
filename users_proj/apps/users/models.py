from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "ID: " + str(self.id) + ", First Name: " + str(self.first_name) + ", Last Name: " + str(self.last_name) + ", Username: " + str(self.username) + ", Email: " + str(self.email)