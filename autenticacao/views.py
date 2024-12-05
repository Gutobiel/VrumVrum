from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from fpdf import FPDF
from django.http import HttpResponse
from django.core.mail import EmailMessage
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

    @staticmethod
    def gerar_pdf():
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
        pdf.output(pdf_buffer, 'S')  # 'S' indica que o PDF deve ser retornado como string

        pdf_buffer.seek(0)  # Posiciona o ponteiro no início do buffer
        return pdf_buffer

class EnviarRelatorioEmailView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        print("View chamada com sucesso.")
        pdf_buffer = RelatorioView.gerar_pdf()
        pdf_content = pdf_buffer.getvalue()

        email = EmailMessage(
            subject="Relatório de Veículos",
            body="Segue em anexo o relatório de veículos em formato PDF.",
            to=["gutobielsantos@sempreceub.com"],  # Altere para a lista de destinatários desejada
        )
        email.attach('relatorio_veiculos.pdf', pdf_content, 'application/pdf')
        email.send()
        pdf_buffer.close()  # Fecha o buffer após o uso

        return HttpResponse("E-mail enviado com sucesso.")
