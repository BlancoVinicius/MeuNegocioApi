import os
import base64
import hashlib

# Função para gerar o code_verifier
def generate_code_verifier():
    verifier = os.urandom(32)  # 32 bytes aleatórios
    code_verifier = base64.urlsafe_b64encode(verifier).decode('utf-8').rstrip("=")
    return code_verifier

# Função para gerar o code_challenge com o método S256 (SHA-256)
def generate_code_challenge(code_verifier):
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').rstrip("=")
    return code_challenge

# Gerar o code_verifier e code_challenge
code_verifier = generate_code_verifier()
code_challenge = generate_code_challenge(code_verifier)

# Definir o code_challenge_method
code_challenge_method = "S256"  # Método recomendado

# Imprimir os valores gerados
print("Code Verifier:", code_verifier)
print("Code Challenge:", code_challenge)
print("Code Challenge Method:", code_challenge_method)
