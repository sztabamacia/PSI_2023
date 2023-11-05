from django.db import models

# Create your models here.


class Autor(models.Model):
    autorID = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)


class Wypozyczenie(models.Model):
    idWypozyczenia = models.IntegerField(primary_key=True)
    dataWypozyczenia = models.DateField()
    dataZwrotu = models.DateField()


class Klient(models.Model):
    idKlient = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=100, default="")
    nazwisko = models.CharField(max_length=100, default="")
    klient_wypozyczenie = models.ForeignKey(Wypozyczenie, on_delete=models.CASCADE, null=True, blank=True)
    adres = models.CharField(max_length=200)
    email = models.EmailField()
    nrtel = models.IntegerField()


class Ksiazka(models.Model):
    idKsiazki = models.IntegerField(primary_key=True)
    tytul = models.CharField(max_length=100, default="")
    autorID = models.ForeignKey(Autor, on_delete=models.CASCADE)
    rokWydania = models.IntegerField()
    wypozyczenie = models.ForeignKey(Wypozyczenie, on_delete=models.CASCADE)
    dostepnosc = models.BooleanField()



