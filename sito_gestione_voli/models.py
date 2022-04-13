from mailbox import NoSuchMailboxError
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.




'''
class prenotazione:
    andata = models.CharField(max_length=200)
    ritorno = models.CharField(max_length=200)
    date_andate = models.DateField() #assicurati che si scriva così
    date_ritorno = models.DateField()
    neonati = models.SmallIntegerField()
    bambini = models.SmallIntegerField()
    adulti = models.SmallIntegerField()
    
class volo:
    personale = JsonField... #json (tizio caio muzio)
    posti totali
    posti disponibili


class immagini_sito(models.Model):
    sfondo = models.ImageField()
    logo = models.ImageField()
    
Class Personale
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    sesso = models.CharField(max_length=20)
    id ruolo = models.CharField(max_length=100) # l'id è il ruolo, così colleghi tutto il personale
    luogo = models.CharField(max_length=200)

Class Ruolo:
    Assistente = models.CharField(max_length=100)
    Pilota = models.CharField(max_length=100)
    ass_Pilota = models.CharField(max_length=100)
    Hostess_di_volo = models.CharField(max_length=100)
    Hostess_di_terra = models.CharField(max_length=100)
    ass_airport = models.CharField(max_length=100)
    Addetto_di_Scalo = models.CharField(max_length=100) #quelli che vendono i biglietti fisicamente
    Steward_terra = models.CharField(max_length=100)
    


class Airport(models.Model): 
    personale = JsonField... #json (tizio caio muzio)
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


'''
#{%load 'sito_gestione_voli/sfondo.gif' static%}