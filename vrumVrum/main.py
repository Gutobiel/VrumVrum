from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def minha_view(request):
    nome_usuario = request.user.username
    return render(request, 'meu_template.html', {'nome_usuario': nome_usuario})
