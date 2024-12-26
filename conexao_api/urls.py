from django.contrib import admin
from django.urls import path
from conexao_api import views

app_name = 'api'

urlpatterns = [
    path('', views.login, name='teste'),
]
