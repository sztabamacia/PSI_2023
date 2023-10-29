from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def default_view(request):
    return HttpResponse("To jest defaultowy widok.")