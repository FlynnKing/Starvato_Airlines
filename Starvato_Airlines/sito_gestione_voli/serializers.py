from dataclasses import fields
from rest_framework import serializers
from.models import *

class AirportSerialized(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class AircraftSerialized(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class FlySerialized(serializers.ModelSerializer):
    class Meta:
        model = Fly
        fields = '__all__'

class PrenotazioneSerialized(serializers.ModelSerializer):
    class Meta:
        model = Prenotazione
        fields = '__all__'

class RuoloSerialized(serializers.ModelSerializer):
    class Meta:
        model = Ruolo
        fields = '__all__'

class PersonaleSerialized(serializers.ModelSerializer):
    class Meta:
        model = Personale
        fields = '__all__'
