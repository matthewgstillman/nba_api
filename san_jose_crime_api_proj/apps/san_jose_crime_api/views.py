from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = "https://moto.data.socrata.com/resource/wrmr-tdyp.json"
    response = requests.get(url)
    # crime = response.json()
    # print("Crime:{}".format(crime))
    # print("Response: {}".format(response))
    context = {
    }
    return render(request, 'san_jose_crime_api/index.html', context)