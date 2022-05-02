from django import forms
from .models import Fly

<<<<<<< HEAD
class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['partenza','arrivo','date_andata','date_ritorno']

#class PrenotazioneForm(forms.ModelForm):
#    class Meta:
#        model = Prenotazione
#        fields = ['andata_e_o_ritorno','partenza','arrivo','date_andate','date_ritorno','neonati','bambini','adulti']
=======
class PrenotazioneForm(forms.ModelForm):
    class Meta:
        model = Prenotazione
        fields = ['partenza', 'arrivo', 'date_andate', 'date_ritorno', 'neonati', 'bambini', 'adulti', 'andata_e_o_ritorno']

class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['Aircraft', 'tot_passeggeri', 'partenza', 'arrivo', 'date_andata', 'date_ritorno']
>>>>>>> 929c82bcea3a3252b68e97e648774a5f5fa549d3



#'unique_id','name','surname','email','address','city','state','zip_code','fly','fly_seat',