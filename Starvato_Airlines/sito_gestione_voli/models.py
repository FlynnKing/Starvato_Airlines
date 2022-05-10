
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.id

# CON BLANK DICI CHE IL CAMPO NON E' NECESSARIO 
class Aircraft(models.Model):
    name = models.CharField(max_length=200)
    locate = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    tot_posti = models.IntegerField( default=60)

    class Meta:
        verbose_name = 'Aereo'
        verbose_name_plural = 'Aerei'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.id

class FlyHistory(models.Model):
    Aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)
    tot_passeggeri = models.IntegerField( default=60)
    partenza = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "_inizio")
    arrivo = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "_fine")
    date_andata = models.DateField(default=now)
    date_ritorno = models.DateField(default=now, blank=True)
class Fly(models.Model):
    Aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)
    tot_passeggeri = models.IntegerField( default=60)
    partenza = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "inizio")
    arrivo = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "fine")
    date_andata = models.DateField(default=now)
    date_ritorno = models.DateField(default=now, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.id
        history = FlyHistory()
        history.Aircraft = self.Aircraft
        history.tot_passeggeri = self.tot_passeggeri
        history.partenza = self.partenza
        history.arrivo = self.arrivo
        history.date_andata = self.date_andata
        history.date_ritorno = self.date_ritorno

class PrenotazioneHistory(models.Model):
    partenza = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "_start")
    arrivo = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "_end")
    date_andate = models.DateField() #assicurati che si scriva così
    date_ritorno = models.DateField() #la riga di sopra e questa sarnno presi dall'aereo...
    neonati = models.SmallIntegerField()
    bambini = models.SmallIntegerField()
    adulti = models.SmallIntegerField()
    andata_e_o_ritorno = models.CharField(max_length=50)
class Prenotazione(models.Model):
    partenza = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "start")
    arrivo = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name = "end")
    data_andata = models.DateField() #assicurati che si scriva così
    data_ritorno = models.DateField() #la riga di sopra e questa sarnno presi dall'aereo...
    neonati = models.SmallIntegerField()
    bambini = models.SmallIntegerField()
    adulti = models.SmallIntegerField()
    andata_e_o_ritorno = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.id
        history = PrenotazioneHistory()
        history.partenza = self.partenza
        history.arrivo = self.arrivo
        history.date_andate = self.data_andata
        history.date_ritorno = self.data_ritorno
        history.neonati = self.neonati
        history.bambini = self.bambini
        history.adulti = self.adulti
        history.andata_e_o_ritorno = self.andata_e_o_ritorno

# pip install django-widget-tweaks INSTALLALO
class Personale(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    sesso = models.CharField(max_length=20)
    SCELTE = (
        (1, 'Assistente'), 
        (2, 'Pilota'), 
        (3, 'Assistente Pilota'), 
        (4, 'puttana volante'), 
        (5, 'puttana di terra'), 
        (6, 'assistente di volo'), 
        (7, 'Adetto di Scalo'), 
        (8, 'Steward terra'))
    ruolo = models.IntegerField(
        choices=SCELTE,
        default=1,
    )
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.id