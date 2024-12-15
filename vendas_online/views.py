from django.shortcuts import render
from vendas_online.models import FormCadastro
# Create your views here.
def index(request):
    return render(request, 'templates_vendas_onlina/entrada.html')

def login(request):
    return render(request, 'templates_vendas_onlina/login.html')

def cadastrar(request):
    
    form = FormCadastro()

    return render(
        request, 'templates_vendas_onlina/cadastrar.html',
        {'form': form}
    )