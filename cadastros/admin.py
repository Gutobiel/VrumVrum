from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Cargo, Orgao
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'celular')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Additional info'), {'fields': ('cargo', 'orgao', 'setor', 'status', 'observacoes')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'celular', 'cargo', 'orgao', 'setor', 'status', 'groups', 'observacoes'),
        }),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active', 'cargo', 'orgao')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cargo)
admin.site.register(Orgao)

