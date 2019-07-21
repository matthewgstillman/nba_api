from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    url = ("https://api.genius.com/oauth/authorize?                        client_id=bbgbwThMyJzgUxDRvzpvfd02u4DGOkqxCt6cT2CZ63ZvWDhUT5t160vPc_g32hm5&redirect_uri=www.nowebsite.com&scope=REQUESTED_SCOPE&state=SOME_STATE_VALUE&response_type=code")
    return render(request, 'rap_genius_api/index.html')