from django.shortcuts import render, redirect
import requests
import lyricsgenius as genius

# Create your views here.
def index(request):
    defs = ud.define('netflix and chill')
    print(defs)
    context = {
    }
    return render(request, 'urban_dictionary/index.html', context)