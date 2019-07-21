from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, RegistrationForm

# Create your views here.
def index(request):
    form = RegistrationForm()
    context = {
        'form': form
    }
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!") 
            return render(request, 'movie_reviewer/index.html', {'form': form })
        else:
            form = RegistrationForm()
    return render(request, 'movie_reviewer/index.html', {'form': form })

def register(request): 
    form = RegistrationForm()
    context = {
        'form': form
    }
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return render('movie_reviewer/register.html', {'form': form })
        else:
            form = RegistrationForm()  
            context = {
                'form': form
            }
    return render(request, 'movie_reviewer/register.html', context )


def users(request):
    context = {
        'users': users
    }
    return render(request, 'movie_reviewer/users.html', context)