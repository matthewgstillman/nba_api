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
    meta = nba_players['meta']
    print(meta)
    data = nba_players['data']
    print(data)
    for i in range(0, len(data)):
        print(data[i])
        first_name = data[i]['first_name']
        last_name = data[i]['last_name']
        height_inches = data[i]['height_inches']
        height_feet = data[i]['height_feet']
        weight_pounds = data[i]['weight_pounds']
        team = data[i]['team']
        conference = data[i]['team']['conference']
        city = data[i]['team']['city']
        name = data[i]['team']['name']
        division = data[i]['team']['division']
        abbreviation = data[i]['team']['abbreviation']
        full_name = data[i]['team']['full_name']
        team_id = data[i]['team']['id']
        position = data[i]['position']
        player_id = data[i]['id']
        print("My name is {} {} and I play for the {}. I'm {} foot {} inches tall and weigh {} pounds.".format(first_name, last_name, full_name, height_feet, height_inches, weight_pounds))
        players = {
            "first_name": first_name,
            "last_name": last_name,
            "height_inches": height_inches,
            "height_feet": height_feet,
            "weight": weight_pounds,
            "team": team,
            "city": city,
            "name": name,
            "division": division,
            "abbreviation": abbreviation,
            "full name": full_name,
            "team id": team_id,
            "position": position,
            "player id": player_id
        }
    return render(request, 'nba_api/index.html', players)

def players(request):
    return render(request, 'nba_api/players.html')