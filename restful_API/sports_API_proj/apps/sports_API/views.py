from django.shortcuts import render
import base64
import requests
# Create your views here.
def index(request):
    print "Shit Sandwich"   
    return render(request, 'sports_API/index.html')


def send_request(request):
    print "Shit Sandwiches"
    response = requests.get(
        url={'https://api.mysportsfeeds.com/v1.2/pull/nba/2018-playoff/game_boxscore.json?gameid=20180425-MIN-HOU&teamstats=W,L,PTS,PTSA&playerstats=2PA,2PM,3PA,3PM,FTA,FTM'},
        params={
            "fordate": "20161121"
        },
        headers={
            "Authorization": "Basic " + base64.b64encode('{}:{}'.format({'matt_stillman'},{'SuperBowl50'}).encode('utf-8')).decode('ascii')
        }
        )
    print "Shit sandwich"
    sports_data = response.json()
    context = {
        'sports_data': sports_data,
        'response': response,
    }
    # Not printing - Not working - Lame
    print response
    print sports_data
    return render(request, 'sports_API/index.html', context)