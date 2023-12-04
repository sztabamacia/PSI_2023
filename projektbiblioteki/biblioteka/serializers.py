from django.utils import timezone
from rest_framework import serializers

from .models import Wypozyczenie, Klient, Ksiazka, Autor


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    autorID = serializers.IntegerField()
    imie = serializers.CharField(max_length=100)
    nazwisko = serializers.CharField(max_length=100)

    class Meta:
        model = Autor
        fields = ['autorID', 'imie', 'nazwisko']


class WypozyczenieSerializer(serializers.HyperlinkedModelSerializer):
    idWypozyczenia = serializers.IntegerField()
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

        if value <= timezone.now().date():
            raise serializers.ValidationError("Data zwrotu musi być w przyszłości")
        return value


class KlientSerializer(serializers.HyperlinkedModelSerializer):
    idKlient = serializers.IntegerField()
    imie = serializers.CharField(max_length=100)
    nazwisko = serializers.CharField(max_length=100)
    klient_wypozyczenie = serializers.SlugRelatedField(queryset=Wypozyczenie.objects.all(), slug_field='idWypozyczenia')
    adres = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    nrtel = serializers.IntegerField()

    class Meta:
        model = Klient
        fields = ['idKlient', 'imie', 'nazwisko', 'klient_wypozyczenie', 'adres', 'email', 'nrtel']

    def validate_email(self, value):
        # sprawdzamy czy ten email już należy do jakiegoś klienta
        if Klient.objects.filter(email=value).exclude(idKlient=self.instance.idKlient).exists():
            raise serializers.ValidationError("ten email już jest zajęty")
        return value

    def validate_nrtel(self, value):
        if Klient.objects.filter(nrtel=value).exclude(idKlient=self.instance.idKlient).exists():
            raise serializers.ValidationError("ten numer telefonu już jest zajęty")
        return value


class KsiazkiSerializer(serializers.HyperlinkedModelSerializer):
    idKsiazki = serializers.IntegerField()
    tytul = serializers.CharField(max_length=100)
    autorID = serializers.HyperlinkedRelatedField(
        view_name='autor-detail',
        read_only=True
    )
    rokWydania = serializers.IntegerField()
    wypozyczenie = serializers.HyperlinkedRelatedField(
        view_name='wypozyczenie-detail',
        read_only=True
    )
    dostepnosc = serializers.BooleanField()
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Ksiazka
        fields = ['idKsiazki', 'tytul', 'autorID', 'rokWydania', 'wypozyczenie', 'dostepnosc','owner']

    def validate_dostepnosc(self, value):
        if value and self.instance.idWypozyczenia is not None:
            raise serializers.ValidationError("Książka jest już wypożyczona")
        return value



