from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    return render(request, 'movies_api/index.html')

def movies(request):
    url = ("https://api.internationalshowtimes.com/v4/movies/")
    response = requests.get(url)
    movies = response.json()
    # genre = movies.movies['genre']
    print(response)
    print(movies)
    context = {
        'response': response,
        'movies': movies,
    }
    return render(request, 'movies_api/movies.html', context)
