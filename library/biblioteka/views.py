from .models import *
from .serializers import *
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def default_view(request):
    return HttpResponse("To jest defaultowy widok.")


def klient_list(request):
    klienci = Klient.objects.all()
    serializer = KlientSerializer(klienci, many=True)
    return JsonResponse(serializer.data, safe=False)


def wypozyczenie_list(request):
    wypoz = Wypozyczenie.objects.all()
    serializer = WypozyczenieSerializer(wypoz, many=True)
    return JsonResponse(serializer.data, safe=False)


def autor_list(request):
    aut = Autorzy.objects.all()
    serializer = AutorzySerializer(aut, many=True)
    return JsonResponse(serializer.data, safe=False)


def ksiazki_list(request):
    ksia = Ksiazki.objects.all()
    serializer = KsiazkiSerializer(ksia, many=True)
    return JsonResponse(serializer.data, safe=False)
