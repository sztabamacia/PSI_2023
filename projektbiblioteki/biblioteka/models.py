from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Autor(models.Model):
    autorID = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Wypozyczenie(models.Model):
    idWypozyczenia = models.IntegerField(primary_key=True)
    dataWypozyczenia = models.DateField()
    dataZwrotu = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='wypozyczenie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dataWypozyczenia} {self.dataZwrotu}'



class Klient(models.Model):
    idKlient = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=100, default="")
    nazwisko = models.CharField(max_length=100, default="")
    klient_wypozyczenie = models.ForeignKey(Wypozyczenie, on_delete=models.CASCADE, null=True, blank=True)
    adres = models.CharField(max_length=200)
    email = models.EmailField()
    nrtel = models.IntegerField()

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Ksiazka(models.Model):
    idKsiazki = models.IntegerField(primary_key=True)
    tytul = models.CharField(max_length=100, default="")
    autorID = models.ForeignKey(Autor, on_delete=models.CASCADE)
    rokWydania = models.IntegerField()
    wypozyczenie = models.ForeignKey(Wypozyczenie, on_delete=models.CASCADE, null=True, blank=True)
    dostepnosc = models.BooleanField()
    owner = models.ForeignKey('auth.User', related_name='ksiazka', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.tytul} {self.rokWydania}'



