from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Секој бенд се карактеризира со име, име на држава од каде потекнува, година на формирање и број на одржани настапи.

class Band(models.Model):
    def __str__(self):
        return self.ime
    ime = models.CharField(max_length=100)
    imeDrzava = models.CharField(max_length=100, null=True, blank=True)
    godinaFormiranje = models.IntegerField(default=0)
    brojOdrzaniNastani = models.IntegerField(default=0)

##Секој настан се карактеризира со име, датум и
# време на одржување на настанот, постер, корисник кој го креирал настанот, бендови кои настапуваат на настанот,
# информација дали настанот е на отворено или не.

class Event(models.Model):
    ime = models.CharField(max_length=100)
    vremeOdrzuvanje = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    kreator = models.ForeignKey(User, on_delete=models.CASCADE)
    daliENaOtvoreno = models.BooleanField(default=False)

class BandEvent(models.Model):
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)

