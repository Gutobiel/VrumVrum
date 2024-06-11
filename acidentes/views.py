from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PaginaAcidentesView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'acidentes/acidentes.html'

