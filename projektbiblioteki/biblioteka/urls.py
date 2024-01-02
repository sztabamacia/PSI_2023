from django.urls import path
from . import views

urlpatterns = [
    path('autor/', views.AutorList.as_view(), name='autor-list'),
    path('autor/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),
    path('wypozyczenie/', views.WypozyczenieList.as_view(), name='wypozyczenie-list'),
    path('wypozyczenie/<int:pk>/', views.WypozyczenieDetail.as_view(), name='wypozyczenie-detail'),
    path('klient/', views.KlientList.as_view(), name='klient-list'),
    path('klient/<int:pk>/', views.KlientDetail.as_view(), name='klient-detail'),
    path('ksiazka/', views.KsiazkaList.as_view(), name='ksiazka-list'),
    path('ksiazka/<int:pk>/', views.KsiazkaDetail.as_view(), name='ksiazka-detail'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api/klient/', views.KlientList.as_view())

]