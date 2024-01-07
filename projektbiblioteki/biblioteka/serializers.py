from django.utils import timezone
from rest_framework import serializers
from datetime import datetime

from .models import Wypozyczenie, Klient, Ksiazka, Autor


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    autorID = serializers.IntegerField(required=False)
    imie = serializers.CharField(max_length=100)
    nazwisko = serializers.CharField(max_length=100)

    class Meta:
        model = Autor
        fields = ['autorID', 'imie', 'nazwisko']

    def validate_autorID(self, value):
        if self.instance is not None:
            query = Autor.objects.filter(autorID=value).exclude(autorID=self.instance.autorID)
        else:
            query = Autor.objects.filter(autorID=value)
        if query.exists():
            raise serializers.ValidationError("ten id już jest zajęty")
        return value


class WypozyczenieSerializer(serializers.HyperlinkedModelSerializer):
    idWypozyczenia = serializers.IntegerField(required=False)
    dataWypozyczenia = serializers.DateField()
    dataZwrotu = serializers.DateField()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Wypozyczenie
        fields = ['idWypozyczenia', 'dataWypozyczenia', 'dataZwrotu','owner']

    def validate_dataWypozyczenia(self, value):
    # sprawdzamy czy data wypożyczenia nie jest z przyszłości
        if value > timezone.now().date():
            raise serializers.ValidationError("Data wypożyczenia nie może być z przyszłości")
        return value

    def validate_dataZwrotu(self, value):
        if value < timezone.now().date():  # changed from <= to <
            raise serializers.ValidationError("Data zwrotu musi być w przyszłości")
        return value
    
    def validate_idWypozyczenia(self, value):
        if self.instance is not None:
            query = Wypozyczenie.objects.filter(idWypozyczenia=value).exclude(idWypozyczenia=self.instance.idWypozyczenia)
        else:
            query = Wypozyczenie.objects.filter(idWypozyczenia=value)
        if query.exists():
            raise serializers.ValidationError("ten id już jest zajęty")
        return value


class KlientSerializer(serializers.HyperlinkedModelSerializer):
    idKlient = serializers.IntegerField(required=False)
    imie = serializers.CharField(max_length=100)
    nazwisko = serializers.CharField(max_length=100)
    klient_wypozyczenie = serializers.SlugRelatedField(queryset=Wypozyczenie.objects.all(), slug_field='idWypozyczenia',allow_null=True)
    adres = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    nrtel = serializers.IntegerField()

    class Meta:
        model = Klient
        fields = ['idKlient', 'imie', 'nazwisko', 'klient_wypozyczenie', 'adres', 'email', 'nrtel']

    def validate_email(self, value):
        # sprawdzamy czy ten email już należy do jakiegoś klienta
        if self.instance is not None:
            query = Klient.objects.filter(email=value).exclude(idKlient=self.instance.idKlient)
        else:
            query = Klient.objects.filter(email=value)
        if query.exists():
            raise serializers.ValidationError("ten email już jest zajęty")
        return value

    def validate_nrtel(self, value):
        if self.instance is not None:
            query = Klient.objects.filter(nrtel=value).exclude(idKlient=self.instance.idKlient)
        else:
            query = Klient.objects.filter(nrtel=value)
        if query.exists():
            raise serializers.ValidationError("ten numer telefonu już jest zajęty")
        return value
    
    def validate_idKlient(self, value):
        if self.instance is not None:
            query = Klient.objects.filter(idKlient=value).exclude(idKlient=self.instance.idKlient)
        else:
            query = Klient.objects.filter(idKlient=value)
        if query.exists():
            raise serializers.ValidationError("ten id już jest zajęty")
        return value

class KsiazkiSerializer(serializers.HyperlinkedModelSerializer):
    idKsiazki = serializers.IntegerField(required=False)
    tytul = serializers.CharField(max_length=100)
    autorID = serializers.SlugRelatedField(
        queryset=Autor.objects.all(),
        slug_field='autorID'
    )
    rokWydania = serializers.IntegerField()
    wypozyczenie = serializers.HyperlinkedRelatedField(
    queryset=Wypozyczenie.objects.all(),
    view_name='wypozyczenie-detail',
    allow_null=True,
)
    dostepnosc = serializers.BooleanField()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ksiazka
        fields = ['idKsiazki', 'tytul', 'autorID', 'rokWydania', 'wypozyczenie', 'dostepnosc','owner']

    def validate_rokWydania(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Rok wydania nie może być w przyszłości")
        return value
    
    



