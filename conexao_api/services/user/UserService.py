from urllib.parse import urlencode
from django.http import HttpResponseNotFound
import json, requests

from conexao_api.models.models import UserToken
from conexao_api.services.user.acces_token import ConexaoApi

#importes para teste


class UserTokenService:
    
    @staticmethod
    def generate_code(request):
        conexao = ConexaoApi()

        base_url = 'https://auth.mercadolivre.com.br/authorization?'

        params = {
            'response_type': 'code',
            'client_id': '5823365826124083',
            'redirect_uri': 'https://www.google.com.br/',
            'code_challenge': conexao.code_challenge,
            'code_challenge_method': 'S256'
        }
        # Verifica se o token existe
        token = UserToken.objects.filter(user=request.user).first()

        #Cria o token se o token nao existir
        if token is None:
            token = UserToken.objects.create(
                user=request.user,
                code_verifier= conexao.code_verifier,
                access_token=None,
                refresh_token=None,
                user_id_api=None
            )
        else:
            # Atualiza o code_verifier
            token.code_verifier = conexao.code_verifier 
            token.save()
        # Adiciona o token ao dicionário de parâmetros
        query_string = urlencode(params)
        # Concatena a URL base com a query string
        url = f"{base_url}{query_string}"
        # Redireciona para a URL
        return url
    

    @staticmethod
    def get_access_token(request): # recebe o request + o code (falta implementar parametro o code)
         # param_url = request.GET['code']
        code="TG-678d6231d9842d0001afd9a2-2179923685"
    
        # recupera o code_verifier
        user = request.user
        token = UserToken.objects.get(user=user)
        code_verifier = token.code_verifier
        # cria o token
        conexao = ConexaoApi()
        response = conexao.get_token(code, code_verifier)

        # verifica se a requisição foi bem-sucedida e se o token foi criado
        if response.status_code not in [200, 201]: 
            return HttpResponseNotFound("Pagina não encontarada: " + str(response.status_code) )
            
        # se o token foi criado, converte a resposta em um dicionário
        response = json.loads(response.text)
        
        # recupera os dados do token
        access_token = response.get('access_token')
        user_id_api = response.get('user_id')
        refresh_token = response.get('refresh_token')
        
        # atualiza os dados do token
        token.access_token = access_token
        token.refresh_token = refresh_token
        token.user_id_api = user_id_api

        # salvar dados no banco
        token.save()

        return response
    

    @staticmethod
    def get_refresh_token(request):
        # recupera o token
        token = UserToken.objects.get(user=request.user)
        # recupera o refresh_token
        refresh_token = token.refresh_token
        
        conexao = ConexaoApi()
        # renova o token
        response = conexao.refresh_token(refresh_token)
        # verifica se a requisição foi bem-sucedida
        if response is not None and response.status_code not in {200, 201}:
            raise UserToken.DoesNotExist

        response_json = json.loads(response.text)
        # recupera os dados do token
        access_token = response_json.get('access_token')
        refresh_token = response_json.get('refresh_token')

        # atualiza os dados do token
        token.access_token = access_token
        token.refresh_token = refresh_token
        token.save() # salvar dados no banco

        # retorna a resposta
        return response.json()
    

    @staticmethod
    def verificar_token_acesso(request):
        url = 'https://api.mercadolibre.com/users/me'
        # recupera o token
        token = UserToken.objects.filter(user=request.user).first()
        # verifica se o token existe
        if token.access_token is None:
            # se o token nao existir, redireciona para a pagina do mercado livre
            raise AttributeError("access_token não existe!")
            
        # cria o header da requisição
        headers = {
            'Authorization': f'Bearer {token.access_token}'
        }
        # faz a requisição
        response = requests.get(url, headers=headers)
        # verifica se a requisição foi bem-sucedida
        if response.status_code not in [200, 201]: 
            # se nao for inválido, redireciona para a refresh token
            return response.raise_for_status()
        # se for váido, redireciona para a home
        return response.json()
        