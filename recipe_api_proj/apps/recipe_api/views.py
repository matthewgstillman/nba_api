from django.shortcuts import render, redirect
from api_key import api_key, food_keys
import requests

# Create your views here.
def index(request):
    app_key = api_key['app_key']
    print("App Key: " + str(app_key))
    app_id = api_key['app_id']
    print("App ID: " + str(app_id))
    url_root = "https://api.edamam.com/search?q=chicken&app_id=$"
    url_app_id = app_id
    url_middle = "&app_key=$"
    url_app_key = app_id
    # url_format = "&format=json"
    url_tail = "&from=0&to=3&calories=591-722&health=alcohol-free"
    url = str(url_root) + str(url_app_id) + str(url_middle) + str(url_app_key) + str(url_tail)
    print("URL: " + str(url))
    response = requests.get(url)
    # recipes = response.json()
    print(response)
    # url = "https://api.edamam.com/search?q=chicken&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}&from=0&to=3&calories=591-722&health=alcohol-free"
    context = {
        # 'recipes': recipes,
    }
    return render(request, 'recipe_api/index.html', context)

