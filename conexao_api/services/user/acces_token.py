import requests
from utils.gerar_code_verifier import *
from var_ambiente import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
# Create your models here.

class ConexaoApi:
    def __init__(self):
        self.code_verifier = code_verifier
        self.code_challenge = code_challenge
        self.code_challenge_method = code_challenge_method
        self.code = self.get_code()

    def get_code(self):
        pass

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


api = ConexaoApi()
api.get_token()
