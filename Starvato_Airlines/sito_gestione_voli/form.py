from django import forms
from .models import Fly, Prenotazione

class PrenotazioneForm(forms.ModelForm):
    class Meta:
        model = Prenotazione
        fields = ['partenza', 'arrivo', 'date_andate', 'date_ritorno', 'neonati', 'bambini', 'adulti', 'andata_e_o_ritorno']

class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['Aircraft', 'tot_passeggeri', 'partenza', 'arrivo', 'date_andata', 'date_ritorno']



#'unique_id','name','surname','email','address','city','state','zip_code','fly','fly_seat',