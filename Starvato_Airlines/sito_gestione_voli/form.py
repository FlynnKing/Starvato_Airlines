from django import forms
from .models import Fly

class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['partenza','arrivo','date_andata','date_ritorno']

#class PrenotazioneForm(forms.ModelForm):
#    class Meta:
#        model = Prenotazione
#        fields = ['andata_e_o_ritorno','partenza','arrivo','date_andate','date_ritorno','neonati','bambini','adulti']




#'unique_id','name','surname','email','address','city','state','zip_code','fly','fly_seat',