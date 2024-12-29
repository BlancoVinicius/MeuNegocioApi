from django.shortcuts import render,redirect
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required

from conexao_api.models import UserToken
from conexao_api.services.user.acces_token import ConexaoApi

#importes para teste
from django.http import JsonResponse, HttpResponseNotFound
import json, requests

# Create your views here.

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

    token = UserToken.objects.filter(user=request.user).first()

    if token is None:
        token = UserToken.objects.create(
            user=request.user,
            code_verifier= conexao.code_verifier,
            access_token=None,
            refresh_token=None,
            user_id_api=None
        )
    else:
        token.code_verifier = conexao.code_verifier 
        token.save()

    query_string = urlencode(params)
    url = f"{base_url}{query_string}"
    return redirect(url)

@login_required
def get_access_token(request):

    # param_url = request.GET['code']
    code="TG-676f171f09b9ce00017564fd-2178079091"
    
    # buscar no banco de dados
    user = request.user
    token = UserToken.objects.get(user=user)
    code_verifier = token.code_verifier

    conexao = ConexaoApi()
    response = conexao.get_token(code, code_verifier)

    if response.status_code != 200 or response.status_code != 201: 
        return HttpResponseNotFound("Pagina não encontarada: " + str(response.status_code))
    
    response = json.loads(response.text)
    
    access_token = response.get('access_token')
    user_id_api = response.get('user_id')
    refresh_token = response.get('refresh_token')

    token.access_token = access_token
    token.refresh_token = refresh_token
    token.user_id_api = user_id_api

    # salvar dados no banco
    token.save()

    return JsonResponse(response)

@login_required
def get_refresh_token(request):
    
    token = UserToken.objects.get(user=request.user)

    refresh_token = token.refresh_token
    print(refresh_token)
    conexao = ConexaoApi()
    
    response = conexao.refresh_token(refresh_token)
    
    if response != None and response.status_code == 200 or response.status_code == 201:
        response_json = json.loads(response.text)
        access_token = response_json.get('access_token')
        refresh_token = response_json.get('refresh_token')

        token.access_token = access_token
        token.refresh_token = refresh_token
        print(refresh_token)
        token.save()

    return JsonResponse(response.json())

@login_required
def verificar_token_acesso(request):
    try:

        url = 'https://api.mercadolibre.com/users/me'
        token = UserToken.objects.filter(user=request.user).first()
        
        if token.access_token is None:
            return redirect('api:code_mercado_livre')
        
        headers = {
            'Authorization': f'Bearer {token.access_token}'
        }
        
        response = requests.get(url, headers=headers)
        
        if not response.status_code == 200 or not response.status_code == 201:
            return redirect('api:refresh_token')
        
        return redirect('vendas_online:home')
    except AttributeError as e:
        return redirect('api:code_mercado_livre')
