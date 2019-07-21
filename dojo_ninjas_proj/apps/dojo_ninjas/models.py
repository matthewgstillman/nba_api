from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NinjaManager(models.Manager):
    def create_ninja(self, postData):
        pass

class Ninja(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NinjaManager()

    def __unicode__(self):
        return "ID: " + str(self.id) + ", First Name: " + str(self.first_name) + ", Last Name: " + str(self.last_name)

class DojoManager(models.Manager):
    def create_dojo(self, postData):
        pass

class Dojo(models.Model):
    location = models.CharField(max_length=50)
    student = models.ForeignKey(Ninja, related_name="students", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DojoManager()

    def __unicode__(self):
        return "ID: " + str(self.id) + ", Location: " + str(self.location)