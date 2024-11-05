from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
from .models import CustomUser, Cargo, Orgao, generate_random_password


class CustomUserCreationForm(UserCreationForm):
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um cargo'}))
    orgao = forms.ModelChoiceField(queryset=Orgao.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    status = forms.ChoiceField(choices=CustomUser.STATUS_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = [
            'nome_completo',
            'username',
            'email',
            'celular',
            'cargo',
            'setor',
            'orgao',
            'groups',
            'status',
            'observacoes',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Se é um novo usuário (cadastro)
            self.fields['password1'].required = False
            self.fields['password2'].required = False
            self.fields['password1'].widget.attrs['placeholder'] = 'Deixe em branco para gerar uma senha automaticamente'
            self.fields['password2'].widget.attrs['placeholder'] = 'Deixe em branco para gerar uma senha automaticamente'

    def clean_email(self):
            email = self.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError(f"O email {email} já está em uso.")
            return email

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            user.password = make_password(password)
        else:
            user.set_password(generate_random_password())
        if commit:
            user.save()
            self.save_m2m()
        return user

class CustomUserChangeForm(UserChangeForm):
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um cargo'}))
    orgao = forms.ModelChoiceField(queryset=Orgao.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    status = forms.ChoiceField(choices=CustomUser.STATUS_CHOICES, widget=forms.RadioSelect)
    password = forms.CharField(label="Senha", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Deixe em branco para manter a senha atual'}))

    class Meta:
        model = CustomUser
        fields = [ # Adicionar os campos
            'nome_completo',
            'username',
            'email',
            'celular',
            'cargo',
            'setor',
            'orgao',
            'groups',
            'status',
            'observacoes',
            'password', 
        ]
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.set_password(password)
        if commit:
            user.save()
            self.save_m2m()
        return user


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']

    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )