from django.db import models

# Create your models here.

class Donnee(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    temperature = models.FloatField(max_length=100)
    id_capteur = models.ForeignKey("Capteur", on_delete=models.DO_NOTHING, default=None)

class Capteur(models.Model):
    maison = models.CharField(max_length=100)
    piece = models.CharField(max_length=100)
    id_capteur = models.CharField(max_length=100)