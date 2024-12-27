from django.db import models


# Create your models here.

from django.db import models
from django.contrib.auth.models import User  # Importando o modelo de usuário do Django

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')  # Relaciona com o usuário
    code_verifier = models.CharField(max_length=255, blank=True, null=True)  # Código do verificador
    access_token = models.CharField(max_length=255, blank=True, null=True)  # Token de acesso
    refresh_token = models.CharField(max_length=255, blank=True, null=True)  # Token de atualização
    user_id_api = models.CharField(max_length=255, blank=True, null=True)  # ID do usuário na API

    def __str__(self):
        return f'Token for {self.user.username}'
