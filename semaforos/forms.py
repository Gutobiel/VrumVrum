from django import forms
from .models import Semaforo

class SemaforoForm(forms.ModelForm):
    class Meta:
        model = Semaforo
        fields = ['codigo', 'endereco', 'tipo', 'marca', 'modelo']
