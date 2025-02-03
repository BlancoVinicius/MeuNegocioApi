from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import requests
from conexao_api.models import UserToken

#importes para teste
from django.http import JsonResponse
from conexao_api.services.user.UserService import UserTokenService

# Create your views here.

@login_required
def get_code(request):

    url =  UserTokenService.generate_code(request)
    return redirect(url)


@login_required
def get_access_token(request):

    response = UserTokenService.get_access_token(request)
    return JsonResponse(response)


@login_required
def get_refresh_token(request):
    
    try:
        response = UserTokenService.get_refresh_token(request)
        return JsonResponse(response)
    except UserToken.DoesNotExist as e:
            return redirect('vendas_online:home')


@login_required
def verificar_token_acesso(request):
    
    try:
        response = UserTokenService.verificar_token_acesso(request)
        return JsonResponse(response)
    except AttributeError as e:
        return redirect('api:code_mercado_livre')
    except requests.HTTPError as e:
         return redirect('api:refresh_token')

def publicar_item(request):
     pass


from .forms import ProductForm
import json
@login_required
def create_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Salvar o objeto Product no banco de dados
            # j = json.loads(form.data)
            # print(j)
            data = json.loads(request.POST.get('pictures'))
            return JsonResponse(data)
            # return redirect('product_list')  # Redirecionar para a lista de produtos, por exemplo
    
    form = ProductForm()
    return render(request, 'templates_conexao_api/criar_produtos.html', {'form': form})
