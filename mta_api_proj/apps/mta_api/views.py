from django.shortcuts import render, redirect
import requests
import json
from api_key import api_key

# Create your views here.
def index(request):
    url_root = 'http://datamine.mta.info/mta_esi.php?key='
    key = api_key['key']
    url_tail = '&feed_id=1'
    # og_url = 'http://datamine.mta.info/mta_esi.php?key=<key>&feed_id=1'
    url = str(url_root) + str(key) + str(url_tail)
    print("Url: {}".format(url))
    response = requests.get(url)
    subways = response.json()
    context = {
        # 'subways': subways,
    }
    return render(request, 'mta_api/index.html')