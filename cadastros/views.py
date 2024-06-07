from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import login
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .forms import GroupForm
from django.contrib.auth.models import Group
from .models import CustomUser, generate_random_password, generate_random_string


class RegisterView(LoginRequiredMixin, View):
    login_url = '/login/'  # URL de login, se o usuário não estiver autenticado
    redirect_field_name = 'redirect_to'  # Nome do campo de redirecionamento

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'cadastros/index.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = generate_random_string()
            if not user.password:
                user.set_password(generate_random_password())
            user.save()
            login(request, user)
            return redirect('home')
        return render(request, 'cadastros/index.html', {'form': form})


########### ATUALIZAR OS DADOS DE UM USUARIO ###############

class UpdateUserView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'lista/editar-usuario.html'

    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        form = CustomUserChangeForm(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, self.template_name, {'form': form})
    
############ EXCLUIR UM USUARIO ##############

class DeleteUserView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'lista/excluir-usuario.html'

    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        return render(request, self.template_name, {'user': user})

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return redirect('user_list')
    

############# LISTAR OS USUARIOS ##############

class UserListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'lista/usuarios.html'

    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, self.template_name, {'users': users})


from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import GroupForm



############## CRIAR GRUPO DE USUÁRIOS ##############

class GroupCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'grupos/criar_grupos.html'
    def get(self, request):
        form = GroupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            form.save_m2m()  # Para salvar as permissões associadas
            return redirect('group_list')
        return render(request, self.template_name, {'form': form})
    

############# ATUALIZAR GRUPO DE USUÁRIOS ##############

class GroupUpdateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'grupos/editar_grupos.html'
    def get(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        form = GroupForm(instance=group)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect('group_list')
        return render(request, self.template_name, {'form': form})
    

############# EXCLUIR GRUPO DE USUÁRIOS ##############
    

class GroupDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'grupos/excluir_grupos.html'
    def get(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        return render(request, self.template_name, {'group': group})

    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        return redirect('group_list')
    

############# LISTAR GRUPO DE USUÁRIOS ##############

class GroupListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'grupos/listar_grupos.html'
    def get(self, request):
        groups = Group.objects.all()
        return render(request, self.template_name, {'groups': groups})
