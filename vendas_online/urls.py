from django.contrib import admin
from django.urls import path
from vendas_online import views

app_name = 'vendas_online'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
