
from django.shortcuts import render
from .form import *
from .models import *
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

    all_airports = Airport.objects.all()
    # [andata_e_ritorno, soltanto_andata, _andata, _ritorno, _neonati, _bambini, _adulti, date_andata, date_ritorno]

    PreForm = PrenotazioneForm()
    if PreForm.is_valid():
        campiBiglietto = Prenotazione.objects.filter( # devono essere uguali ai campi in form.py
            andata_e_o_ritorno=request.POST['andata_e_o_ritorno'], 
            partenza=request.POST['partenza'], 
            arrivo=request.POST['arrivo'],
            data_andata=request.POST['data_andata'],
            data_ritorno=request.POST['data_ritorno'], 
            neonati=request.POST['neonati'], 
            bambini=request.POST['bambini'],
            adulti=request.POST['adulti']
            )


        allFly = Fly.objects.all()
    flyForm = FlyForm() # creo prima la classe
    if flyForm.is_valid():
        filt = Fly.objects.filter(
            soltanto_andata=request.POST['partenza'], 
            arrive=request.POST['arrivo'], 
            data_andata=request.POST['date_andata'],
            data_ritorno=request.POST['date_ritorno']
            )

        context = {
            'campiBiglietto' : campiBiglietto,
            'all_airports' : all_airports,
            'flyForm' : flyForm,
            'voli' : filt
        }
        
    return render(request, 'sito_gestione_voli/index.html', context)

   


def admin_panel(request):
    return render(request, 'sito_gestione_voli/pannello_amministratore.html')

def riepilogo(request):

    return render(request, 'sito_gestione_voli/posti_riepilogo_dati.html')

