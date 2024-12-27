from django.contrib import admin
from django.urls import path
from conexao_api import views

app_name = 'api'

urlpatterns = [
    path('', views.get_conexao, name='conexao'),
    path('code/', views.get_code, name='code_mercado_livre'),
    path('acces_token/', views.get_access_token, name='acces_token'),
    
]
