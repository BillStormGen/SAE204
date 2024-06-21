from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'domoticapp/capteur/index.html')

def domotic(request):
    return render(request, 'domoticapp/capteur/domotic.html')