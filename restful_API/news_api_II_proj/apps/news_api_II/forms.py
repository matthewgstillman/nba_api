from django import forms
from django.forms import ModelForm
from django.db import models
from .models import User

#Create the form class.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

form = UserForm()