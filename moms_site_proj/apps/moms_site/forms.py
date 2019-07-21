from django import forms
#4/02/2018 Trying to integrate model information - importing Email
# from django.contrib.auth.models import Email

class EmailForm(forms.Form):
    name = forms.CharField(max_length=50)
    email_address = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000)