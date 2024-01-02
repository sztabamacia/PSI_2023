from django.test import TestCase
from rest_framework.test import APITestCase
from .serializers import AutorSerializer, WypozyczenieSerializer, KlientSerializer
from .models import Autor, Wypozyczenie, Klient
from django.utils import timezone
import datetime

from django.contrib.auth.models import User

class TestSerializers(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.autor_attributes = {
            'autorID': 1,
            'imie': 'John',
            'nazwisko': 'Doe'
        }

        self.wypozyczenie_attributes = {
            'idWypozyczenia': 1,
            'dataWypozyczenia': timezone.now().date().isoformat(),
            'dataZwrotu': (timezone.now().date() + datetime.timedelta(days=1)).isoformat(),
            'owner': self.user
        }

        self.klient_attributes = {
            'idKlient': 1,
            'imie': 'Jane',
            'nazwisko': 'Doe',
            'nrtel': 232323232,
            'email': 'sdasdad@sdad',
            'adres': 'kokowa',
            'klient_wypozyczenie': None

        }

        self.autor = Autor.objects.create(**self.autor_attributes)
        self.wypozyczenie = Wypozyczenie.objects.create(**self.wypozyczenie_attributes)
        self.klient = Klient.objects.create(**self.klient_attributes)

    def test_autor_serializer(self):
        serializer = AutorSerializer(instance=self.autor)
        self.assertEqual(serializer.data, self.autor_attributes)

    def test_wypozyczenie_serializer(self):
        serializer = WypozyczenieSerializer(instance=self.wypozyczenie)
        wypozyczenie_data = self.wypozyczenie_attributes.copy()
        wypozyczenie_data['owner'] = self.user.username
        self.assertEqual(serializer.data, wypozyczenie_data)

    def test_klient_serializer(self):
        serializer = KlientSerializer(instance=self.klient)
        self.assertEqual(serializer.data, self.klient_attributes)