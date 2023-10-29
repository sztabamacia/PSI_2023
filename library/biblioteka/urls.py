from django.urls import path
from . import views

urlpatterns = [
    path('default/', views.default_view, name='default_view'),
]