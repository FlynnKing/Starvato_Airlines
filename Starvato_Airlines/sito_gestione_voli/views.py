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
    context = {         # metto le variabili che mi serviranno nella pagina che riutilizzerò con Django
        'all_airports' : all_airports,
        'flyForm':flyForm
    }
    if flyForm.is_valid(): # vedo se i campi sono validi con gli attributi del modello relativo (variabile che descrivi nell'html)
        filt = Fly.objects.filter(soltanto_andata=request.POST['andata_e_o_ritorno'], arrive=request.POST['arrive'], date=request.POST['date'], free_seats__gte = request.POST['persone'])
        #devi cambiare il link del metodo post (nell'HTML), per elaborare i dati in questa pagina
        # con il java fai apparire i voli disponibili con quelle richieste e il pulsante di conferma 
        # dopo di che una volta che l'utentre ha scelto l'aereo di andata o andata e ritorno 
        print(filt)
        context['voli'] = filt
    return render(request, 'sito_gestione_voli/index.html', context)

def admin_panel(request):
    return render(request, 'sito_gestione_voli/pannello_amministratore.html')

def riepilogo(request):

    return render(request, 'sito_gestione_voli/posti_riepilogo_dati.html')

