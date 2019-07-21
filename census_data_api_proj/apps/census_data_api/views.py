from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    url = 'https://demo.ckan.org/api/3/action/group_list'
    response = requests.get(url)
    print("Response: {}".format(response))
    last_year_data = response.json()
    print("2017 Census Data: {}".format(last_year_data))
    context = {
        # 'last_year_data': last_year_data,
    }
    return render(request, 'census_data_api/index.html', context)