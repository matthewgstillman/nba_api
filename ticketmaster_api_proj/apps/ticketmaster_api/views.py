from django.shortcuts import render, redirect
import requests
from api_key import key

# Create your views here.
def index(request):
    api_key = key['api_key']
    url_root = ('https://app.ticketmaster.com/discovery/v2/events.json?apikey=')
    url = str(url_root) + str(api_key)
    response = requests.get(url)
    events = response.json()
    print("Events: \n{}".format(events))
    context = {
        'events': events,
    }
    return render(request, 'ticketmaster_api/index.html', context)