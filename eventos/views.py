from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PaginaEventosView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'eventos/eventos.html'

class AdicionarEventosView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'eventos/adicionar-eventos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        breadcrumb_items = [
            {'name': 'Lista de Eventos', 'link': reverse('eventos')},
            {'name': 'Cadastrar Evento', 'link': None},
        ]
        
        context['breadcrumb_items'] = breadcrumb_items
        return context




