from django.utils import timezone
from rest_framework import serializers

from .models import Wypozyczenie, Klient, Ksiazka, Autor


class AutorSerializer(serializers.Serializer):
    autorID = serializers.IntegerField()
    imie = serializers.CharField(max_length=100)
    nazwisko = serializers.CharField(max_length=100)


class WypozyczenieSerializer(serializers.Serializer):
    idWypozyczenia = serializers.IntegerField()
    dataWypozyczenia = serializers.DateField()
    dataZwrotu = serializers.DateField()

    class Meta:
        model = Wypozyczenie
        fields = ['idWypozyczenia', 'dataWypozyczenia', 'dataZwrotu']

    def validate_dataWypozyczenia(self, value):
        # sprawdzamy czy data wypożyczenia nie jest z przyszłości
        if value > timezone.now().date():
            raise serializers.ValidationError("Data wypożyczenia nie może być z przyszłości")
        return value

    def validate_dataZwrotu(self, value):

        if value <= timezone.now().date():
            raise serializers.ValidationError("Data zwrotu musi być w przyszłości")
        return value


class KlientSerializer(serializers.Serializer):
    idKlient = serializers.IntegerField()
    imie = serializers.CharField(max_length=100)
    nazwisko = serializers.CharField(max_length=100)
    klient_wypozyczenie = serializers.PrimaryKeyRelatedField(queryset=Wypozyczenie.objects.all())
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


class KsiazkiSerializer(serializers.Serializer):
    idKsiazki = serializers.IntegerField()
    tytul = serializers.CharField(max_length=100)
    autorID = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    rokWydania = serializers.IntegerField()
    wypozyczenie = serializers.PrimaryKeyRelatedField(queryset=Wypozyczenie.objects.all())
    dostepnosc = serializers.BooleanField()

    class Meta:
        model = Ksiazka
        fields = ['idKsiazki', 'tytul', 'autorID', 'rokWydania', 'wypozyczenie', 'dostepnosc']

    def validate_dostepnosc(self, value):
        if value and self.instance.idWypozyczenia is not None:
            raise serializers.ValidationError("Książka jest już wypożyczona")
        return value



