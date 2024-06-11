from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PaginaSemaforoView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'semaforos/semaforo.html'

class AdicionarSemaforoView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'semaforos/adicionar-semaforo.html'