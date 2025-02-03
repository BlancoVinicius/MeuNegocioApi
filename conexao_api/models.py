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


class Product(models.Model):
    title = models.CharField(max_length=255)
    category_id = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency_id = "BRL"
    available_quantity = models.PositiveIntegerField(blank=False,null=False)
    buying_mode = "buy_it_now"
    listing_type_id = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    # sale_terms = models.ManyToManyField('SaleTerm')
    pictures = models.JSONField()
    description = models.TextField()
    shipping = models.JSONField()
    attributes = models.JSONField()

    def __str__(self):
        return self.title
    

class SaleTerm(models.Model):
    pass