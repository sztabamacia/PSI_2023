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

    def __str__(self):
        return str(self.idKlient) + ' ' + str(self.nazwisko) + ' - ' + str(self.idWyporzyczenia)


class Wypozyczenie(models.Model):
    idWypozyczenia = models.IntegerField(auto_created=True)
    dataWypozyczenia = models.DateField()
    dataZwrotu = models.DateField()

    def __str__(self):
        return 'ID wypożyczenia:  ' + str(self.idWypozyczenia)


class Ksiazki(models.Model):
    idKsiazki = models.IntegerField(auto_created=True)
    tytul = models.CharField(max_length=100)
    autorID = models.ForeignKey("Autorzy", on_delete=models.CASCADE)
    rokWydania = models.IntegerField()
    idWypozyczenia = models.ForeignKey("Wypozyczenie", on_delete=models.CASCADE)
    dostepnosc = models.BooleanField()

    def __str__(self):
        return 'Id książki: ' + str(self.idKsiazki) + ' ' + 'Id Autora: ' + str(self.autorID) + ' ' + str(self.tytul)


class Autorzy(models.Model):
    autorID = models.IntegerField(auto_created=True)
    imie = models.CharField(max_length=100, blank=True, null=True, default="")
    nazwisko = models.CharField(max_length=100, blank=True, null=True, default="")


    def __str__(self):
        return str(self.imie) + ' ' + str(self.nazwisko) + '  id: ' + str(self.autorID)