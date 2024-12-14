from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templates_vendas_onlina/entrada.html')

def login(request):
    return render(request, 'templates_vendas_onlina/login.html')