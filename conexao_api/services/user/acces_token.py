import requests

import sys
import os

# Adiciona a pasta caminhi da raiz para acesso aos modulos acima desta pasta
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..'))
sys.path.append(caminho_raiz)

from var_ambiente import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from conexao_api.services.utils.gerar_code_verifier import code_verifier, code_challenge, code_challenge_method

# Agora você pode importar o módulo

class ConexaoApi:
    def __init__(self, code:str):
        self.code_verifier = code_verifier
        self.code_challenge = code_challenge
        self.code_challenge_method = code_challenge_method
        self.code = code

    # def get_code(self):
    #     pass

    def get_token(self):
        url = "https://api.mercadolibre.com/oauth/token"

        payload = {
            'grant_type': "authorization_code",
            "client_id":CLIENT_ID,
            "client_secret":CLIENT_SECRET,
            'code': self.code,
            'redirect_uri': REDIRECT_URI,
            'code_verifier': self.code_verifier,
        }

        headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def refresh_token(self):
        url = "https://api.mercadolibre.com/oauth/token"

        payload = {
            'grant_type': 'refresh_token',
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET,
            'refresh_token':'TG-676c9c4962cb2d00011efac6-62073791'
        }

        headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

# api = ConexaoApi()
# api.refresh_token()

