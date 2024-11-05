from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from fpdf import FPDF
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.http import HttpResponse
from autenticacao.forms import PerfilForm
from io import BytesIO
from django.views import View

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


    def get(self, request, *args, **kwargs):
        user = request.user
        form = PerfilForm(instance=user)
        return render(request, self.template_name, {'form': form})
    


class RelatorioView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'pagina-relatorio/relatorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        referer = self.request.META.get('HTTP_REFERER')
        breadcrumb_items = [{'name': 'Menu', 'link': reverse('menu-principal')}]
        if referer:
            breadcrumb_items.append({'name': 'Voltar', 'link': referer})
        breadcrumb_items.append({'name': 'Relatório', 'link': None})
        context['breadcrumb_items'] = breadcrumb_items
        return context

    def gerar_pdf(self):
        data = {
            'Tipo de Veículo': ['Motos', 'Carros', 'Caminhões'],
            'Quantidade': [120, 350, 45]
        }
        df = pd.DataFrame(data)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório de Veículos", ln=True, align='C')
        for index, row in df.iterrows():
            pdf.cell(200, 10, txt=f"{row['Tipo de Veículo']}: {row['Quantidade']}", ln=True)

        pdf_buffer = BytesIO()
        pdf.output(pdf_buffer)
        pdf_buffer.seek(0)
        return pdf_buffer

    def enviar_pdf_por_email(self, request):
        pdf_buffer = self.gerar_pdf()
        email = EmailMessage(
            subject="Relatório de Veículos",
            body="Segue em anexo o relatório de veículos em formato PDF.",
            from_email="seuemail@gmail.com",  # ou use 'EMAIL_HOST_USER' configurado no settings
            to=["destinatario@example.com"],
        )
        email.attach('relatorio_veiculos.pdf', pdf_buffer.getvalue(), 'application/pdf')
        email.send()
        return HttpResponse("E-mail enviado com sucesso.")
    
class EnviarRelatorioEmailView(LoginRequiredMixin, View):
 def get(self, request, *args, **kwargs):
     relatorio_view = RelatorioView()
     return relatorio_view.enviar_pdf_por_email(request)



