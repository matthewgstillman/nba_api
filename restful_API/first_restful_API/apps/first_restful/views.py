from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    return render(request, 'first_restful/index.html')

def home(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    print geodata
    #changed name of app after request to 'first_restful/home.html' instead of 'core/home.html'
    return render(request, 'first_restful/home.html', {
        'ip': geodata['ip'],
        'city': geodata['city'],
        'state': geodata['region_name'],
        'state_abbreviation': geodata['region_code'],
        'zip': geodata['zip_code'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyAImfZi_RlGbZ8yFjFzYH4GTdBrf2VtrdA',
        #Updated on 4/23 to add brand new google maps API key
        #Updated this to add my Google Maps API Key from yesterday 4/22
        #Normally don't put in above line! Hide and protect the API key!
        'is_cached': is_cached
    })

