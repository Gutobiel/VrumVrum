from django.shortcuts import render

def menu(request):
    return render(request, 'semaforos/tela_menu.html')

def acidentes(request):
    return render(request, 'semaforos/tela_acidentes.html')

def adicionar_semaforos(request):
    return render(request, 'semaforos/tela_adicionar_semaforos.html')

def controle_semaforos(request):
    return render(request, 'semaforos/tela_controle_semaforos.html')

def sobre(request):
    return render(request, 'semaforos/tela_sobre_nos.html')

def suporte(request):
    return render(request, 'semaforos/tela_suporte.html')
