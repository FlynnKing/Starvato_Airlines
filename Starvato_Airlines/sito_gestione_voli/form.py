from django import forms
from .models import Fly, Prenotazione

class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['partenza','arrivo','date_andata','date_ritorno']

class PrenotazioneForm(forms.ModelForm):
    class Meta:
        model = Prenotazione
        fields = ['andata_e_o_ritorno','partenza','arrivo','data_andata','data_ritorno','neonati','bambini','adulti']