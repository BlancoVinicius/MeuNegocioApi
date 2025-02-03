from django.contrib import admin
from django.urls import path
from conexao_api import views

app_name = 'api'

urlpatterns = [
    #Rotas para token
    path('code/', views.get_code, name='code_mercado_livre'),
    path('acces_token/', views.get_access_token, name='acces_token'),
    path('refresh_token/', views.get_refresh_token, name='refresh_token'),
    path('verifica_token/', views.verificar_token_acesso, name='verifica_token'),

    #rotas para produtos
    path('publicar/item/', views.create_product, name='publicar_item'),

    # Rotas de pesquisa
    # path('pesquisar/', views.pesquisar, name='pesquisar'),
]
