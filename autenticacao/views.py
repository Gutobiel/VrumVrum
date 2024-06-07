from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home/index.html'

class MenuPrincipalView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'pagina-menu/pagina-menu.html'

class AdminPaginaView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'pagina-admin/admin.html'

