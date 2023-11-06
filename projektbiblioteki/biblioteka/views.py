from rest_framework import generics
from .models import Autor, Ksiazka, Klient, Wypozyczenie
from .serializers import AutorSerializer, KsiazkiSerializer, KlientSerializer, WypozyczenieSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import *


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class WypozyczenieList(generics.ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer

class WypozyczenieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    permission_classes = [IsAdminUser]

class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkiSerializer
    permission_classes = [IsAdminUser]


class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

