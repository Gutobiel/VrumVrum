from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home/index.html'

class SobreNosView(TemplateView):
    template_name = 'home/sobre.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['pagina_atual'] = 'sobre'
        return contexto

class SuporteView(TemplateView):
    template_name = 'home/suporte.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['pagina_atual'] = 'suporte'
        return contexto




class MenuPrincipalView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'pagina-menu/pagina-menu.html'

class AdminPaginaView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'pagina-admin/admin.html'

class PerfilView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'pagina-perfil/perfil.html'

class RelatorioView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'pagina-relatorio/relatorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtém a URL da página anterior do cabeçalho HTTP Referer
        referer = self.request.META.get('HTTP_REFERER')
        
        # Se houver uma URL anterior, adicione-a aos breadcrumbs
        breadcrumb_items = [{'name': 'Menu', 'link': reverse('menu-principal')}]
        if referer:
            breadcrumb_items.append({'name': 'Voltar', 'link': referer})
        
        breadcrumb_items.append({'name': 'Relatório', 'link': None})
        
        context['breadcrumb_items'] = breadcrumb_items
        return context



