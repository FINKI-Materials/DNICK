from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Kategorija(models.Model):
    ime = models.CharField(max_length=50)
    opis = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)

class Klinet(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    adresa = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    ime = models.CharField(max_length=50)
    opis = models.CharField(max_length=50)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.SET_NULL, null=True)
    fotografija = models.ImageField(upload_to='hrana/', null=True, blank=True)
    cena = models.IntegerField()
    kolicina = models.IntegerField()
    kreator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Prodazba(models.Model):
    produkt = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    kolicina = models.IntegerField()
    klinet = models.ForeignKey(Klinet, on_delete=models.SET_NULL, null=True)
