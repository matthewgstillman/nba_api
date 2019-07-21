from django.shortcuts import render, redirect
import json
import requests

def index(request):
    url = ('https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv')
    response = requests.get(url)
    print response
    lebron_data = response.json()
    # print lebron_data
    context = {
        # 'lebron_data': lebron_data,
    }
    return render(request, 'nba_api/index.html', context)