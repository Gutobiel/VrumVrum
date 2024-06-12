from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from semaforos.models import Semaforo



class PaginaAcidentesView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'acidentes/acidentes.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Recupera todos os semáforos
        semaforos = Semaforo.objects.all()
        # Adiciona os semáforos ao contexto
        context['semaforos'] = semaforos
        return context  

