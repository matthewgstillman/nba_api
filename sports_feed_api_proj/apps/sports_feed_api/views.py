from django.shortcuts import render, redirect
import requests
import base64

# Create your views here.
def index(request):
    url = ('https://api.mysportsfeeds.com/v2.0/pull/mlb')
    response = requests.get(url)
    sports = response.json()
    # genre = movies.movies['genre']
    print(response)
    # print(sports)
    context = {
        'response': response,
        'sports': sports,
    }
    return render(request, 'sports_feed_api/index.html', context)

