from django.urls import path 
from . import views

urlpatterns = [
    path('add/', views.enviar, name='enviar'),
    path('lista/', views.lista, name='lista'),
]