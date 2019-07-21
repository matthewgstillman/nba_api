from django.shortcuts import render
from api_key import keys
import requests

# Create your views here.
def index(request):
    strains = []
    url_root = 'http://strainapi.evanbusse.com/'
    api_key = str(keys['key'])
    url_tail = '/strains/search/all'
    url = url_root + api_key + url_tail
    print("URL: {}".format(url))
    response = requests.get(url)
    flowers = response.json()
    print("Flowers: {}".format(flowers))
    for i in flowers:
        strain = flowers[i]
        strains.append(strain)
        print("Strain: {}".format(flowers[i]))
    context = {
        'flowers': flowers,
        'strains': strains,
    }
    return render(request, 'flower_api/index.html', context)