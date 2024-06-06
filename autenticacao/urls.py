from django.urls import path
from .views import HomeView, MenuPrincipalView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu-principal/', MenuPrincipalView.as_view(), name='menu-principal'),

]
