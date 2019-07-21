from django.shortcuts import render, redirect
import requests
import lyricscorpora as lc

# Create your views here.
def index(request):
    artist = lc.Artist("Drake")
    album_list = artist.get_album_list()
    print(album_list)
    context = {
        'album_list': album_list,
    }
    return render(request, 'lyrics_api/index.html', context)