from django.urls import path
from eventos.views import AdicionarEventosView, PaginaEventosView


urlpatterns = [
    path('eventos/', PaginaEventosView.as_view(), name='eventos'),
    path('adicionar-eventos/', AdicionarEventosView.as_view(), name='adicionar-eventos'),

]
