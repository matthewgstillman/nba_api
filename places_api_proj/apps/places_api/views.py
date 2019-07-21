from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    url = ("https://api.internationalshowtimes.com/v4/movies/")
    return render(request, 'places_api/index.html')