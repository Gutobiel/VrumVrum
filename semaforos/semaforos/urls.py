# semaforos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),  # Página inicial do menu
    path('acidentes/', views.acidentes, name='acidentes'),
    path('adicionar_semaforos/', views.adicionar_semaforos, name='adicionar_semaforos'),
    path('controle_semaforos/', views.controle_semaforos, name='controle_semaforos'),
    path('sobre/', views.sobre, name='sobre'),
    path('suporte/', views.suporte, name='suporte'),
]
