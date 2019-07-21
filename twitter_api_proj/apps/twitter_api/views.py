from django.shortcuts import render, redirect
import twitter
import requests
import twython as Twython
import tweepy
# Create your views here.
def index(request):
    ACCESS_TOKEN = 'j2aSXfK69kPeYtlsvNflnFCVM'
    ACCESS_SECRET = 'dNnFAuLytOoqk0PPb3yu5aN9PLdDph06CDKSKeG0ueYqMoQnNy'
    CONSUMER_KEY = '165917647-s4la36KehkWdQax3HRY8vEDK8GZY6RjAuywJOucf'
    CONSUMER_SECRET = 'Ai7so883VsbbBF522g2YKEpOduhZGjhJL0BxJabzMjHhZ'
    twitter = Twython(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY,CONSUMER_SECRET)
    api_url = 'https://api.twitter.com/1.1/search/tweets.json'
    constructed_url = twitter.construct_api_url(api_url, q='python',
    result_type='popular')
    print constructed_url
    context = {
    }
    return render(request, 'twitter_api/index.html', context)