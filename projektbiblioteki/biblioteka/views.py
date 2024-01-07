from rest_framework import generics
from .models import Autor, Ksiazka, Klient, Wypozyczenie
from .serializers import AutorSerializer, KsiazkiSerializer, KlientSerializer, WypozyczenieSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-list'
    ordering_fields = ['imie','nazwisko']
    search_fields = ['nazwisko']
    filterset_fields = ['imie','nazwisko']


class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-detail'


class WypozyczenieFilter(FilterSet):
    old_date = DateTimeFilter(field_name='dataWypozyczenia',lookup_expr='gte')
    new_date = DateTimeFilter(field_name='dataWypozyczenia',lookup_expr='lte')

    class Meta:
        model = Wypozyczenie
        fields = ['old_date','new_date']


class WypozyczenieList(generics.ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    ordering_fields = ['dataWypozyczenia', 'dataZwrotu']
    search_fields = ['idWypozyczenia']
    filterset_class = WypozyczenieFilter
    name = 'wypozyczenie-list'
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class WypozyczenieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    name = 'wypozyczenie-detail'


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'
    permission_classes = [IsAdminUser]
    ordering_fields = ['nazwisko','adres']
    search_fields = ['nazwisko']


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'
    permission_classes = [IsAuthenticatedOrReadOnly]

class KsiazkaFilter(FilterSet):
    old = NumberFilter(field_name='rokWydania', lookup_expr='gt')
    new = NumberFilter(field_name='rokWydania', lookup_expr='lt')

    class Meta:
        model = Ksiazka
        fields = ['old', 'new']


class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkiSerializer
    permission_classes = [IsAdminUser]
    ordering_fields = ['tytul', 'rokWydania']
    filterset_class = KsiazkaFilter
    name = 'ksiazka-list'
    search_fields = ['tytul']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



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

