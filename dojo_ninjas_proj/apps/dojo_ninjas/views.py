from django.shortcuts import render
from .models import Ninja, Dojo

# Create your views here.
def index(request):
    dojos = Dojo.objects.all()
    print "Dojos: {}".format(dojos)
    ninjas = Ninja.objects.all()
    print "Ninjas: {}".format(ninjas)
    context = {
        'dojos': dojos,
        'ninjas': ninjas
    }
    return render(request, 'dojo_ninjas/index.html', context)