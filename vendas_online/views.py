from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('vendas_online:home')
    return render(request, 'templates_vendas_onlina/entrada.html')

def login(request):
    return redirect('/accounts/login/')
    # return render(request, 'templates_vendas_onlina/login.html')

@login_required(login_url='/login/')
def home(request):

    return render(
        request, 'templates_vendas_onlina/home.html',
    )


# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def teste(request):
#     name = request.POST.get('nome')
#     idade = request.POST.get('idade')
#     return HttpResponse(f"{name} {idade}")