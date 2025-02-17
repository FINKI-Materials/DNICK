from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pilot(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    godinaRagjanje = models.CharField(max_length=50)
    vkuspnoCasoviLetano = models.IntegerField()
    cinVoKompanija = models.CharField(max_length=50)

class Ballon(models.Model):
    tip = models.CharField(max_length=50)
    imeProizveduvac = models.CharField(max_length=50)
    maxPatnici = models.IntegerField()

class Aviokompanija(models.Model):
    ime = models.CharField(max_length=50)
    godinaOsnovanje = models.CharField(max_length=50)
    letaNadvorOdEvropa = models.BooleanField()

class AviokompanijaPilot(models.Model):
    aviokompanija = models.ForeignKey(Aviokompanija, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

class Let(models.Model):
    sifra = models.CharField(max_length=50)
    aerodromSletuva = models.CharField(max_length=50)
    aerodromPoletuva = models.CharField(max_length=50)
    kreator = models.ForeignKey(User, on_delete=models.CASCADE)
    fotografija = models.ImageField(upload_to="flights/",null=True, blank=True)
    balon = models.ForeignKey(Ballon, on_delete=models.SET_NULL, null=True)
    pilot = models.ForeignKey(Pilot, on_delete=models.SET_NULL,  null=True)
    aviokompanija = models.ForeignKey(Aviokompanija, on_delete=models.SET_NULL,  null=True)
