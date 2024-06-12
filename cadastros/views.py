from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.contrib.auth import login
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .forms import GroupForm
from django.contrib.auth.models import Group
from braces.views import GroupRequiredMixin
from .models import CustomUser, generate_random_password, generate_random_string


class RegisterView(GroupRequiredMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    template_name = 'cadastros/index.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        breadcrumb_items = [
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Lista de Funcionários', 'link': reverse('user_list')},
            {'name': 'Cadastrar Funcionário', 'link': None},
        ]
        return render(request, self.template_name, {'form': form, 'breadcrumb_items': breadcrumb_items})


    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = generate_random_string()
            if not user.password:
                user.set_password(generate_random_password())
            user.save()
            login(request, user)
            return redirect('menu-principal')
        return render(request, self.template_name, {'form': form})
    


########### ATUALIZAR OS DADOS DE UM USUARIO ###############

class UpdateUserView(GroupRequiredMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    template_name = 'lista/editar-usuario.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        form = CustomUserChangeForm(instance=user)
        
        breadcrumb_items = [
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Lista de Funcionários', 'link': reverse('user_list')},
            {'name': 'Editar Dados de Cadastro', 'link': None},
        ]
        
        return render(request, self.template_name, {'form': form, 'breadcrumb_items': breadcrumb_items})

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, self.template_name, {'form': form})
    

    
############ EXCLUIR UM USUARIO ##############

class DeleteUserView(GroupRequiredMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    template_name = 'lista/excluir-usuario.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'user': user})

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        user.delete()
        return redirect('user_list')
    

############# LISTAR OS USUARIOS ##############

class UserListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'lista/usuarios.html'

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        breadcrumb_items = [
            {'name': 'Menu', 'link': reverse('menu-principal')},
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Lista de Funcionários', 'link': None},
        ]
        return render(request, self.template_name, {'users': users, 'breadcrumb_items': breadcrumb_items})

############## CRIAR GRUPO DE USUÁRIOS ##############

class GroupCreateView(GroupRequiredMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    template_name = 'grupos/criar_grupos.html'

    def get(self, request, *args, **kwargs):
        form = GroupForm()
        
        breadcrumb_items = [
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Perfis de Acesso', 'link': reverse('group_list')},
            {'name': 'Cadastrar Grupo de Usuário', 'link': None},
        ]
        
        return render(request, self.template_name, {'form': form, 'breadcrumb_items': breadcrumb_items})

    def post(self, request, *args, **kwargs):
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('group_list')
        
        breadcrumb_items = [
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Perfis de Acesso', 'link': reverse('group_list')},
            {'name': 'Cadastrar Grupo de Usuário', 'link': None},
        ]
        
        return render(request, self.template_name, {'form': form, 'breadcrumb_items': breadcrumb_items})


    
############# ATUALIZAR GRUPO DE USUÁRIOS ##############

class GroupUpdateView(GroupRequiredMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    template_name = 'grupos/editar_grupos.html'
    

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        form = GroupForm(instance=group)
        
        breadcrumb_items = [
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Perfis de Acesso', 'link': reverse('group_list')},
            {'name': 'Editar Permissões de Usuário', 'link': None},
        ]
        
        return render(request, self.template_name, {'form': form, 'breadcrumb_items': breadcrumb_items})


    def post(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect('group_list')
        
        breadcrumb_items = [
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Perfis de Acesso', 'link': reverse('group_list')},
            {'name': 'Editar Permissões de Usuário', 'link': None},
        ]
        
        return render(request, self.template_name, {'form': form, 'breadcrumb_items': breadcrumb_items})
    


############# EXCLUIR GRUPO DE USUÁRIOS ##############
    
class GroupDeleteView(GroupRequiredMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    template_name = 'grupos/excluir_grupos.html'

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'group': group})

    def post(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        group.delete()
        return redirect('group_list')
    

############# LISTAR GRUPO DE USUÁRIOS ##############

class GroupListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'grupos/listar_grupos.html'


    def get(self, request, *args, **kwargs):
        groups = Group.objects.all()
        breadcrumb_items = [
            {'name': 'Menu', 'link': reverse('menu-principal')},
            {'name': 'Administração', 'link': reverse('administracao')},
            {'name': 'Lista de Perfis de Acesso', 'link': None},
        ]
        return render(request, self.template_name, {'groups': groups, 'breadcrumb_items': breadcrumb_items})