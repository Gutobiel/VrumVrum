from django.shortcuts import render
from django.http import HttpResponse

def addSemaforo(request): #teste de renderização
    return render(request, 'semaforo/addSemaforo.html')

def logar(request):
    return HttpResponse("Você está na página de login")
  
def cadastro(request):
    return HttpResponse("Você está na página de cadastro")

