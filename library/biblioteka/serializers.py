from rest_framework import serializers
from .models import *


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class WypozyczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = '__all__'


class KsiazkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazki
        fields = '__all__'


class AutorzySerializer(serializers.ModelSerializer):
    class Meta:
        model = Autorzy
        fields = '__all__'
