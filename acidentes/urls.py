from django.urls import path
from acidentes.views import PaginaAcidentesView


urlpatterns = [
    path('acidentes/', PaginaAcidentesView.as_view(), name='acidentes'),

]
