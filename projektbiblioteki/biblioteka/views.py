from rest_framework import generics
from .models import Autor, Ksiazka, Klient, Wypozyczenie
from .serializers import AutorSerializer, KsiazkiSerializer, KlientSerializer, WypozyczenieSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import *
from rest_framework.response import Response
from rest_framework.reverse import reverse


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-list'

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-detail'

class WypozyczenieList(generics.ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    name = 'wypozyczenie-list'

class WypozyczenieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    name = 'wypozyczenie-detail'

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'
    permission_classes = [IsAdminUser]


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'
    permission_classes = [IsAuthenticatedOrReadOnly]


class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkiSerializer
    name = 'ksiazka-list'
    permission_classes = [IsAdminUser]


class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkiSerializer
    name = 'ksiazka-detail'
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'autorzy': reverse(AutorList.name, request=request),
                         'ksiazki': reverse(KsiazkaList.name, request=request),
                         'klienci': reverse(KlientList.name, request=request),
                         'wypozyczenia': reverse(WypozyczenieList.name, request=request)
                         })

