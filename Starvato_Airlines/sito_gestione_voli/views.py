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
    flyForm = FlyForm() # creo prima la classe
    context = {
        'all_airports' : all_airports,
        'flyForm':flyForm
    }
    if flyForm.is_valid(): # vedo se i campi sono validi con gli attributi del modello relativo
        people = request.POST['persone']
        filt = Fly.objects.filter(start=request.POST['start'], arrive=request.POST['arrive'], date=request.POST['date'], free_seats__gte = request.POST['persone'])
        
    
    return render(request, 'sito_gestione_voli/index.html', context)

def admin_panel(request):
    return render(request, 'sito_gestione_voli/pannello_amministratore.html')

def riepilogo(request):
    return render(request, 'sito_gestione_voli/posti_riepilogo_dati.html')

