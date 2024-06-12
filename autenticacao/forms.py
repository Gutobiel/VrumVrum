from django import forms
from cadastros.models import CustomUser

class PerfilForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nome_completo', 'username', 'email', 'celular', 'cargo', 'setor', 'orgao', 'password']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'disabled': 'disabled'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'disabled': 'disabled'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'disabled': 'disabled'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'disabled': 'disabled'}),
            'cargo': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled', 'disabled': 'disabled'}),
            'setor': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'disabled': 'disabled'}),
            'orgao': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled', 'disabled': 'disabled'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': '**********', 'disabled': 'disabled'}),
        }
