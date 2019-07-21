from django.shortcuts import render, redirect
import requests
import WunderWeather


# Create your views here.
def index(request):
    return render(request, 'weather_forecast_api/index.html')