from django.shortcuts import render, redirect
import requests
import lyricscorpora as lc

# Create your views here.
def index(request):
    # api_key = 'yzDudLIsM32qDiezI2NzJumYXRZdXmsrgzmQcMEds'
    # # headers = {'X-API-Key': 'yzDudLIsM32qDiezI2NzJumYXRZdXmsrgzmQcMEds'}
    # #url doesn't work - API-KEY not properly formatted
    # url = ('https://api.propublica.org/campaign-finance/v1/yzDudLIsM32qDiezI2NzJumYXRZdXmsrgzmQcMEds')
    # response = requests.get(url, headers = {'X-API-Key': 'yzDudLIsM32qDiezI2NzJumYXRZdXmsrgzmQcMEds'})
    # campaign_finance = response.json()
    # print campaign_finance
    return render(request, 'pro_publica_campaign_api/index.html')