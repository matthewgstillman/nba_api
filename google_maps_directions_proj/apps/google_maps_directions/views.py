from django.shortcuts import render, redirect
import googlemaps
import requests
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'google_maps_directions/index.html')