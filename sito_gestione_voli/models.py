from mailbox import NoSuchMailboxError
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Airport(models.Model): 
    #personale = JsonField #json (tizio caio muzio)
    ident = models.CharField(max_length=200)
    ttpe = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    elevation_ft = models.CharField(max_length=200)
    continent = models.CharField(max_length=200)
    iso_country = models.CharField(max_length=200)
    iso_region = models.CharField(max_length=200)
    municipality = models.CharField(max_length=200)
    gps_code = models.CharField(max_length=200)
    iata_code = models.CharField(max_length=200)
    local_code = models.CharField(max_length=200)
    coordinates = models.CharField(max_length=200)

class Fly:
    

class Aircraft:
    name = models.CharField(max_length=200)
    locate = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=50)

class prenotazione(models.Model):
    andata = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, relative_name = "start")
    ritorno = models.CharField(Airport, on_delete=models.SET_NULL, null=True, relative_name = "end")
    date_andate = models.DateField() #assicurati che si scriva così
    date_ritorno = models.DateField()
    neonati = models.SmallIntegerField()
    bambini = models.SmallIntegerField()
    adulti = models.SmallIntegerField()

class Ruolo(models.Model):
    Assistente = models.CharField(max_length=100)
    Pilota = models.CharField(max_length=100)
    ass_Pilota = models.CharField(max_length=100)
    Hostess_di_volo = models.CharField(max_length=100)
    Hostess_di_terra = models.CharField(max_length=100)
    ass_airport = models.CharField(max_length=100)
    Addetto_di_Scalo = models.CharField(max_length=100) #quelli che vendono i biglietti fisicamente
    Steward_terra = models.CharField(max_length=100)
    
class Personale(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    sesso = models.CharField(max_length=20)
    ruolo = models.CharField(Ruolo, on_delete=models.SET_NULL, null=True)
    luogo = models.CharField(max_length=200)