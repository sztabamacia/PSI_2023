from django.db import models

# Create your models here.
class Klient(models.Model):
    idKlient=models.IntegerField(auto_created=True)
    imie = models.CharField(max_length=100, blank=True, null= True, default="")
    nazwisko = models.CharField(max_length=100, blank=True, null=True, default="")
    idWyporzyczenia = models.ForeignKey("Wypozyczenie", on_delete=models.CASCADE)
    adres = models.CharField(max_length=200)
    email = models.EmailField()
    nrtel = models.IntegerField()


class Wypozyczenie(models.Model):
    idWypozyczenia = models.IntegerField(auto_created=True)
    dataWypozyczenia = models.DateField()
    dataZwrotu = models.DateField()


class Ksiazki(models.Model):
    idKsiazki = models.IntegerField(auto_created=True)
    tytul = models.CharField(max_length=100)
    autorID = models.ForeignKey("Autorzy", on_delete=models.CASCADE)
    rokWydania = models.IntegerField()
    idWypozyczenia = models.ForeignKey("Wypozyczenie", on_delete=models.CASCADE)
    dostepnosc = models.BooleanField()

class Autorzy(models.Model):
    autorID = models.IntegerField(auto_created=True)
    imie = models.CharField(max_length=100, blank=True, null=True, default="")
    nazwisko = models.CharField(max_length=100, blank=True, null=True, default="")