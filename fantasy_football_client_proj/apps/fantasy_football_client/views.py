from django.shortcuts import render, redirect
import espnff
from espnff import League

# Create your views here.
def index(request):
    league_id = 446679
    year = 2018
    league = League(league_id, year)
    print (league)
    context = {
        'league': league,
    }
    return render(request, 'fantasy_football_client/index.html', context)