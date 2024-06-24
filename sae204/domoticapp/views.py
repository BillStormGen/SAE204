from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'domoticapp/capteur/index.html')


def domotic(request):
    capteurs = Capteur.objects.all()
    donnees_par_capteur = {}

    for capteur in capteurs:
        donnees = Donnee.objects.filter(id_capteur=capteur).order_by('date', 'heure')
        donnees_par_capteur[capteur] = donnees

    context = {
        'donnees_par_capteur': donnees_par_capteur,
    }
    return render(request, 'domoticapp/capteur/domotic.html', context)


def filtrer_donnees(request):
    form = FiltrerDonneesForm(request.GET)
    donnees_par_capteur = {}

    if form.is_valid():
        nom_capteur = form.cleaned_data.get('nom_capteur')
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        heure_debut = form.cleaned_data.get('heure_debut')
        heure_fin = form.cleaned_data.get('heure_fin')
        temperature_min = form.cleaned_data.get('temperature_min')
        temperature_max = form.cleaned_data.get('temperature_max')

        capteurs = Capteur.objects.all()

        if nom_capteur:
            capteurs = capteurs.filter(id_capteur__icontains=nom_capteur)

        for capteur in capteurs:
            donnees = Donnee.objects.filter(id_capteur=capteur)

            if date_debut:
                donnees = donnees.filter(date__gte=date_debut)
            if date_fin:
                donnees = donnees.filter(date__lte=date_fin)
            if heure_debut:
                donnees = donnees.filter(heure__gte=heure_debut)
            if heure_fin:
                donnees = donnees.filter(heure__lte=heure_fin)
            if temperature_min is not None:
                donnees = donnees.filter(temperature__gte=temperature_min)
            if temperature_max is not None:
                donnees = donnees.filter(temperature__lte=temperature_max)

            donnees = donnees.order_by('date', 'heure')
            donnees_par_capteur[capteur] = donnees

    context = {
        'donnees_par_capteur': donnees_par_capteur,
        'form': form,
    }

    return render(request, 'domoticapp/capteur/domotic.html', context)