from re import A
from django.http import JsonResponse
from django.shortcuts import render
from requests import post
from serializers import *



#TERZO PARTY imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Airport.objects.all()
        all_obj_db = qs.first()
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
    
    def get(self, request, *args, **kwargs):
        qs = Aircraft.objects.all()
        all_obj_db = qs.first()
        #serialized = PostSerialized(qs, many = True)
        serialized = AircraftSerialized(all_obj_db)
        return Response(serialized.data)



# Create your views here.
def home (request):
    return render(request, 'sito_gestione_voli/index.html')

def admin_panel(request):
    return render(request, 'sito_gestione_voli/pannello_amministratore.html')
#DOMANDE:
# 1. dovrebbe fare le viste, perché si mettono funzioni dove ritornano qualcosa? e poi cosa ritornano?
# 2. 
# 3. 
