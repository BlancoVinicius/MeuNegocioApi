from django.shortcuts import render,redirect
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required

from conexao_api.services.user.acces_token import ConexaoApi

#importes para teste
from django.http import JsonResponse
import json


# Create your views here.
def get_conexao(request):
    return redirect('vendas_online:home')

@login_required
def get_code(request):
    
    conexao = ConexaoApi()

    base_url = 'https://auth.mercadolivre.com.br/authorization?'

    params = {
        'response_type': 'code',
        'client_id': '5823365826124083',
        'redirect_uri': 'https://www.google.com.br/',
        'code_challenge': conexao.code_challenge,
        'code_challenge_method': 'S256'
    }
    # salvar code verifier
    # ..
    print(conexao.code_verifier)

    query_string = urlencode(params)
    url = f"{base_url}{query_string}"
    return redirect(url)

def get_access_token(request):

    # param_url = request.GET['code']
    code="TG-676edbb137b17c00018512f4-2178079091"
    
    # buscar no banco de dados
    # ...
    code_verifier = "XMUqVQ2pdqZOGbYs-Jnk_HWzVcVcJ7ZW6ua2llEbDds"

    conexao = ConexaoApi()
    response = json.loads(conexao.get_token(code, code_verifier))
    
    # salvar dados no banco
    # ...

    return JsonResponse(response)

def get_refresh_token(request):

    # get refresh_token 

    refresh_token = "TG-676edc1f6851a000010bb4a5-2178079091"

    conexao = ConexaoApi()
    response = json.loads(conexao.refresh_token(refresh_token))
    return JsonResponse(response)



