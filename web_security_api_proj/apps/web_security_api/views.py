from django.shortcuts import render, redirect
import requests
from goodreads import client

# Create your views here.
def index(request):
    # url = ('https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata')
    # response = requests.get(url)
    # breaches = response.json()
    context = {
        # 'breaches': breaches
    }
    return render(request, 'web_security_api/index.html', context)