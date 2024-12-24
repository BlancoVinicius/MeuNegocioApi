from django.contrib import admin
from django.urls import path
from vendas_online import views

app_name = 'vendas_online'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='cadastrar'),
    path('', views.index, name='index'),
]
