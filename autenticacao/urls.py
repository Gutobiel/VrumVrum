from django.urls import path
from .views import AdminPaginaView, HomeView, MenuPrincipalView, PerfilView, RelatorioView, SobreNosView, SuporteView, EnviarRelatorioEmailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sobre/', SobreNosView.as_view(), name='sobre'),
    path('suporte/', SuporteView.as_view(), name='suporte'),


    path('menu-principal/', MenuPrincipalView.as_view(), name='menu-principal'),
    path('pagina-admin/', AdminPaginaView.as_view(), name='administracao'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('relatorio/', RelatorioView.as_view(), name='relatorio'),
     path('relatorio/enviar_email/', EnviarRelatorioEmailView.as_view(), name='enviar_relatorio_pdf'),
]
