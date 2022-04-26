from pyexpat import model
from re import S
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
    def __str__(self):
        return self.name



class Aircraft(models.Model):
    name = models.CharField(max_length=200)
    locate = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    

class posti(models.Model):
    class posto(models.TextChoices):
        prima_classe_libero = 'prima classe libero', ('prima classe libero')
        prima_classe_occupato = 'prima classe occupato', ('prima classe occupato')
        seconda_classe_libero = 'seconda classe libero', ('seconda classe libero')
        seconda_classe_occupato = 'seconda classe occupato', ('seconda classe occupato')
    stato_del_posto = models.CharField(
        max_length=40,
        choices=posto.choices,
        default=posto.prima_classe_libero,
    )
    tot_posti = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.stato_del_posto   






class Fly(models.Model):
    Aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)
    tot_passeggeri = models.IntegerField()
    andata = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "inizio")
    ritorno = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "fine")

class Prenotazione(models.Model):
    andata = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "start")
    ritorno = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "end")
    date_andate = models.DateField() #assicurati che si scriva così
    date_ritorno = models.DateField() #la riga di sopra e questa sarnno presi dall'aereo...
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
    ruolo = models.ForeignKey(Ruolo, on_delete=models.SET_NULL, null=True)
    luogo = models.CharField(max_length=200)
    