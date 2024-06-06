from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/index.html'

class MenuPrincipalView(TemplateView):
    template_name = 'pagina-menu/pagina-menu.html'
