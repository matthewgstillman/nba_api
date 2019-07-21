from django.shortcuts import render, redirect
import billboard

# Create your views here.
def index(request):
    chart = billboard.ChartData('hot-100', date='2018-08-28')
    # print("Chart: " + str(chart))
    for data in chart:
        print ("Data: " + str(data))
        chart_topper = chart[0] 
        context = {
            'chart': chart,
            'chart_topper': chart_topper,
        }
        return render(request, 'billboard_api/index.html', context)