from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from forms import UserForm
from django.views.generic import TemplateView

# Create your views here.

# class IndexView(TemplateView):
#     template_name = 'news_api_II/index.html'

#     def get(self, request):
#         form = UserForm()
#         return render(request, 'news_api_II/index.html', {'form': form})


#     def post(self, request):
#         form = UserForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#         context = {
#             'form': form,
#             'first_name': first_name,
#             'last_name': last_name,
#             'username': username,
#             'email': email
#         }
#         return render(request, 'news_api_II/index.html', context)

def index(request):
    if request.method == 'GET': 
        form = UserForm()
    return render(request, 'news_api_II/index.html', {'form': form})
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            print "First Name: " + first_name
            print "Last Name: " + last_name
            print "Username: " + username
            print "Email: " + email
        form.save()
        context = {
            'form': form,
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email
        }
    return render(request, 'news_api_II/index.html', context)