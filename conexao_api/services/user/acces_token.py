import requests

import sys
import os

# Adiciona a pasta caminhi da raiz para acesso aos modulos acima desta pasta
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..'))
sys.path.append(caminho_raiz)

from var_ambiente import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from conexao_api.services.utils._gerar_code_verifier import generate_code_challenge, code_verifier, code_challenge_method

# Agora você pode importar o módulo

class ConexaoApi:
    def __init__(self):
        self.code_verifier = code_verifier
        self.code_challenge = generate_code_challenge(self.code_verifier)
        self.code_challenge_method = code_challenge_method
    
    def get_token(self, code:str,code_verifier:str) -> requests.Response:
        url = "https://api.mercadolibre.com/oauth/token"

        payload = {
            'grant_type': "authorization_code",
            "client_id":CLIENT_ID,
            "client_secret":CLIENT_SECRET,
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'code_verifier': code_verifier,
        }

        headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
        }

        return requests.request("POST", url, headers=headers, data=payload)


    def refresh_token(self, refresh_token:str) -> requests.Response:
        url = "https://api.mercadolibre.com/oauth/token"

        payload = {
            'grant_type': 'refresh_token',
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET,
            'refresh_token':refresh_token
        }

        headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
        }

        return requests.request("POST", url, headers=headers, data=payload)



