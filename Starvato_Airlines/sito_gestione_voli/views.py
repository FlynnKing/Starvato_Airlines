from django.shortcuts import render
from requests import post, get
from .serializers import *



#TERZO PARTY imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
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
    
    context = {
        'all_airports' : all_airports

    }
    return render(request, 'sito_gestione_voli/index.html', context)

def admin_panel(request):
    return render(request, 'sito_gestione_voli/pannello_amministratore.html')

def riepilogo(request):
    return render(request, 'sito_gestione_voli/posti_riepilogo_dati.html')

