from django import forms
from .models import Fly, Prenotazione

class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['andata','ritorno','date_andata','date_ritorno']

class PrenotazioneForm(forms.ModelForm):
    class Meta:
        model = Prenotazione
        fields = ['unique_id','name','surname','email','address','city','state','zip_code','fly','fly_seat',]
