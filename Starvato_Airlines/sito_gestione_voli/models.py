
from django.utils.timezone import now

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
    tot_posti = models.IntegerField( default=60)
    

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
    tot_posti = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True, default=60)
    def __str__(self):
        return self.stato_del_posto   


class Fly(models.Model):
    Aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)
    tot_passeggeri = models.IntegerField( default=60)
    partenza = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "inizio")
    arrivo = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "fine")
    date_andata = models.DateField(default=now)
    date_ritorno = models.DateField(default=now, blank=True)
        

<<<<<<< HEAD
#class Prenotazione(models.Model):
#    partenza = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "start")
#    arrivo = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "end")
#    date_andate = models.DateField() #assicurati che si scriva così
#    date_ritorno = models.DateField() #la riga di sopra e questa sarnno presi dall'aereo...
#    neonati = models.SmallIntegerField()
#    bambini = models.SmallIntegerField()
#    adulti = models.SmallIntegerField()
#    andata_e_o_ritorno = models.CharField(max_length=50)
=======
class Prenotazione(models.Model):
    partenza = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "start")
    arrivo = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "end")
    date_andate = models.DateField() #assicurati che si scriva così
    date_ritorno = models.DateField() #la riga di sopra e questa sarnno presi dall'aereo...
    neonati = models.SmallIntegerField()
    bambini = models.SmallIntegerField()
    adulti = models.SmallIntegerField()
    class andata_e_o_ritorn(models.TextChoices):
        prima_classe_libero = 'prima classe libero', ('prima classe libero')
        prima_classe_occupato = 'prima classe occupato', ('prima classe occupato')
        seconda_classe_libero = 'seconda classe libero', ('seconda classe libero')
        seconda_classe_occupato = 'seconda classe occupato', ('seconda classe occupato')
    andata_e_o_ritorno = models.CharField(
        max_length=40,
        choices=andata_e_o_ritorn.choices,
        default=andata_e_o_ritorn.prima_classe_libero
    )
>>>>>>> 929c82bcea3a3252b68e97e648774a5f5fa549d3



# pip install django-widget-tweaks INSTALLALO



#class andata_o_andata_e_ritorno(models.Model):
#    class partenza(models.TextChoices):
#        andata = 'Solo andata', ('Solo andata')
#        andata_ritorno = 'andata e ritorno', ('andata e ritorno')
#        
#    andata_e_o_ritonro = models.CharField(
#        max_length=25,
#        choices=partenza.choices,
#        default=partenza.andata,
#    )
#    andata_e_o_ritorno = models.ForeignKey(Prenotazione, on_delete=models.SET_NULL, null=True)
#    def __str__(self):
#        return self.andata_e_o_ritonro 

<<<<<<< HEAD

=======
class Ruolo(models.Model):
    Assistente = models.CharField(max_length=100)
    Pilota = models.CharField(max_length=100)
    ass_Pilota = models.CharField(max_length=100)
    Hostess_di_volo = models.CharField(max_length=100)
    Hostess_di_terra = models.CharField(max_length=100)
    ass_airport = models.CharField(max_length=100)
    Addetto_di_Scalo = models.CharField(max_length=100) #quelli che vendono i biglietti fisicamente
    Steward_terra = models.CharField(max_length=100)
>>>>>>> 929c82bcea3a3252b68e97e648774a5f5fa549d3
    
class Personale(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    sesso = models.CharField(max_length=20)
    class Ruolo(models.Model):
        Assistente = 'AS'
        Pilota = 'PI'
        ass_Pilota = 'AP'
        Hostess_di_volo = 'HV'
        Hostess_di_terra = 'HT'
        ass_airport = 'AV'
        Addetto_di_Scalo = 'AS',
        Steward_terra = 'ST'
        SCELTE = [
            (Assistente, 'Assistente'),
            (Pilota, 'Pilota'),
            (ass_Pilota, 'Assistente Pilota'),
            (Hostess_di_volo, 'puttana volante'),
            (Hostess_di_terra, 'puttana di terra'),
            (ass_airport, 'assistente di volo'),
            (Addetto_di_Scalo, 'Adetto di Scalo'),
            (Steward_terra, 'Steward terra'),
        ]
        ruolo = models.CharField(
            max_length=40,
            choices=SCELTE,
            default=Addetto_di_Scalo,
        )
        luogo = models.CharField(max_length=200)
        def is_upperclass(self):
            return self.ruolo in {self.ass_Pilota, self.Hostess_di_terra}
#1) MODELLO
#ENTITY:
#Volo
#Prenotazione
#Aeroporto
#Aereo
#Personale (ok)
#2) distingui il modello dal funzionamento: il volo ha partenza e arrivo, ma viene effettuato da un aereo "disponibile". 
#La prenotazione ha bisogno dell'aereo e del volo che viene effettuato dall'aereo.
#La prenotazione prende il posto dall'aereo
#VOlo prende l'aereo e la sua storia (devi fare la History di tutte le entità), volo ha gli orari di partenza e arrivo
#nelle History ci metti tutte le modifiche, inserimenti e cancellazioni 
