from django.urls import path
from semaforos.views import AdicionarSemaforoView, PaginaSemaforoView

urlpatterns = [
     path('semaforo/', PaginaSemaforoView.as_view(), name='semaforo'),
     path('adicionar-semaforo/', AdicionarSemaforoView.as_view(), name='adicionar-semaforo'),
]
