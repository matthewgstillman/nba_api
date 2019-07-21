from django.shortcuts import render, redirect
from googlemaps import googlemaps
import psycopg2
import gmplot

# Create your views here.
def index(request):
    gmaps = googlemaps.Client(key='AIzaSyBCpcT3_3H3Qd7dZ05uK_HqoQ2id7fz8M8')
    address = '245 N 11th St, San Jose, CA 95112'
    # lat, lng = gmaps.address_to_latlng(address)
    # print lat, lng 
    context = {
        'address': address,
        # 'lat': lat,
        # 'lng': lng,
    }
    return render(request, 'maps_api/index.html', context)


    


