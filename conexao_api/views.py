from django.shortcuts import render,redirect
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required

from conexao_api.services.user.acces_token import ConexaoApi

# Create your views here.
def get_conexao(request):
    return redirect('vendas_online:home')

@login_required
def get_code(request):
    
    base_url = 'https://auth.mercadolivre.com.br/authorization?'

    params = {
        'response_type': 'code',
        'client_id': '5823365826124083',
        'redirect_uri': 'https://www.google.com.br/',
        'code_challenge': 'HWZ4c1w33dSDGaJ80dO6c952A8Xg4wpWznTqKZBmGuI',
        'code_challenge_method': 'S256'
    }
    
    query_string = urlencode(params)
    url = f"{base_url}{query_string}"
    return redirect(url)

def get_access_token(request):

    # param_url = request.GET['code']
    code="TG-676ecf446851a000010af412-2178079091"
    c = ConexaoApi(code)

    return redirect('vendas_online:home')
