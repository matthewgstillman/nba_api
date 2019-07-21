from django.shortcuts import render, redirect
# from nba_api.stats.endpoints import commonplayerinfo
# from nba_api.stats.static import teams, players
from stockxsdk import Stockx

import nba_api, requests, unirest
# Create your views here.
def index(request):
    response = requests.get('https://www.balldontlie.io/api/v1/players')
    nba_players = response.json()
    print(nba_players)
    return render(request, 'nba_api/index.html')

def players(request):
    return render(request, 'nba_api/players.html')