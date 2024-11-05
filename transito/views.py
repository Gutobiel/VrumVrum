from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PaginaTransitoView(LoginRequiredMixin, TemplateView):
    template_name = 'transito/transito.html'
