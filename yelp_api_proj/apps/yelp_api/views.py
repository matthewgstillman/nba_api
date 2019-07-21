from django.shortcuts import render, redirect
import requests
from yelpapi import YelpAPI
import argparse
from pprint import pprint

# Create your views here.
def index(request):
    argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpapi. '
                                                'Visit https://www.yelp.com/developers/v3/manage_app to get the '
                                                'necessary API keys.')
    argparser.add_argument('api_key', type=str, help='Yelp Fusion API Key')
    args = argparser.parse_args()
    yelp_api = YelpAPI(args.10eRGTSFL8Pkgn0nQrYej1qmIR4FzdUwyrCfKs-PcleTyR3-v68JPMIMciapU80bdbE9pz2DHv1gHMkUAmMfm-zM7eqWHtkQyIS-b6ga5QWNWLx0_k0r44yoaKxXW3Yx)
    return render(request, 'yelp_api/index.html')

# def index(request):
#     url = ("https://api.yelp.com/v3/businesses/search")
#     response = requests.get(url)
#     yelp_result = response.json()
#     print(response)
#     print(yelp_result)
#     context = {
#         'response': response,
#         'yelp_result': yelp_result,
#     }
#     return render(request, 'yelp_api/index.html')