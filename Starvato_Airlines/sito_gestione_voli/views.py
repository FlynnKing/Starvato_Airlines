
from django.shortcuts import render
from .form import *
from .models import *
from django.db.models import *
'''
def get(self, request, *args, **kwargs):
    all_airports = Airport.objects.all()
    all_obj_db = all_airports.first()
    #serialized = PostSerialized(qs, many = True)
    serialized = AirportSerialized(all_obj_db)
    return Response(serialized.data)

def get(self, request, *args, **kwargs):
    qs = Aircraft.objects.all()
    all_obj_db = qs.first()
    #serialized = PostSerialized(qs, many = True)
    serialized = AircraftSerialized(all_obj_db)
    return Response(serialized.data)

def get(self, request, *args, **kwargs):
    qs = Fly.objects.all()
    all_obj_db = qs.first()
    #serialized = PostSerialized(qs, many = True)
    serialized = FlySerialized(all_obj_db)
    return Response(serialized.data)

def get(self, request, *args, **kwargs):
    qs = Aircraft.objects.all()
    all_obj_db = qs.first()
    #serialized = PostSerialized(qs, many = True)
    serialized = AircraftSerialized(all_obj_db)
    return Response(serialized.data)

def get(self, request, *args, **kwargs):
    qs = Aircraft.objects.all()
    all_obj_db = qs.first()
    #serialized = PostSerialized(qs, many = True)
    serialized = AircraftSerialized(all_obj_db)
    return Response(serialized.data)

def get(self, request, *args, **kwargs):
    qs = Aircraft.objects.all()
    all_obj_db = qs.first()
    #serialized = PostSerialized(qs, many = True)
    serialized = AircraftSerialized(all_obj_db)
    return Response(serialized.data)
'''

# Create your views here.
def home (request):

    #all_airports = Airport.objects.all()
    # [andata_e_ritorno, soltanto_andata, _andata, _ritorno, _neonati, _bambini, _adulti, date_andata, date_ritorno]
    campiBiglietto = ''
    PreForm = PrenotazioneForm(request.POST)
    if PreForm.is_valid():
        campiBiglietto = Prenotazione.objects.filter( # devono essere uguali ai campi in form.py
            Q(andata_e_o_ritorno=request.POST['andata_e_o_ritorno']) & 
            Q(partenza=request.POST['partenza']) & 
            Q(arrivo=request.POST['arrivo']) &
            Q(data_andata=request.POST['data_andata']) &
            Q(data_ritorno=request.POST['data_ritorno']) &
            Q(neonati=request.POST['neonati']) &
            Q(bambini=request.POST['bambini']) &
            Q(adulti=request.POST['adulti'])
            )

    else:
        print('form non valido')

        #allFly = Fly.objects.all()
#    flyForm = FlyForm() # creo prima la classe
#    if flyForm.is_valid():
#        filt = Fly.objects.filter(
#            soltanto_andata=request.POST['partenza'], 
#            arrive=request.POST['arrivo'], 
#            data_andata=request.POST['date_andata'],
#            data_ritorno=request.POST['date_ritorno']
#            )

    context = {
        'PreForm': PreForm,
        'campiBiglietto' : campiBiglietto,
        #'all_airports' : all_airports,
        #'flyForm' : flyForm,
        #'voli' : filt
    }
        
    return render(request, 'sito_gestione_voli/index.html', context)

   


def admin_panel(request):
    return render(request, 'sito_gestione_voli/pannello_amministratore.html')

def riepilogo(request):

    return render(request, 'sito_gestione_voli/posti_riepilogo_dati.html')

