from django.shortcuts import render, redirect
import requests
import matplotlib as plt

# Create your views here.
def index(request):
    plot = plt.plot([1,2,3,4],[4,7,8,12])
    show_plot = plt.show()
    print(plot)
    print(show_plot)
    context = {
        'plot': plot,
        'show_plot': show_plot
    }
    return render(request, 'map_plot/index.html', context)