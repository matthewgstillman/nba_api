from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    user_workout = models.ForeignKey(Workout, related_name="user_workout_name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()

    def __unicode__(self):
      return "id: " + str(self.id) + ", Email: " + self.email


class Workout(models.Model):
    workout_name = models.CharField(max_length=50)
    duration = models.IntegerField(max_length=200)
    calories = models.IntegerField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = WorkoutManager()

    def __unicode__(self):
      return "id: " + str(self.id) + ", Workout: " + str(self.workout_name) + ", Duration: " + str(self.duration) + ", Calories Burned: " + str(self.calories)