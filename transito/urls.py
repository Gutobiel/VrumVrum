from django.urls import path
from transito.views import PaginaTransitoView 

urlpatterns = [
     path('transito/', PaginaTransitoView.as_view(), name='transito'),
]
