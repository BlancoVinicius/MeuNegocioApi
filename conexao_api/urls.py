from django.contrib import admin
from django.urls import path
from conexao_api import views

app_name = 'api'

urlpatterns = [
    path('code/', views.get_code, name='code_mercado_livre'),
    path('acces_token/', views.get_access_token, name='acces_token'),
    path('refresh_token/', views.get_refresh_token, name='refresh_token'),
    path('teste_token/', views.verificar_token_acesso, name='verifica_token'),
    
]
