from django.urls import path
from . import views

urlpatterns = [
    path('default/', views.default_view, name='default_view'),
    path('klienci/', views.klient_list),
    path('ksiazki/', views.ksiazki_list),
    path('autorzy/', views.autor_list),
    path('wypozyczenie/', views.wypozyczenie_list),
]
