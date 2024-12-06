from django.contrib import admin
from django.urls import path
from vendas_online import views

urlpatterns = [
    path('', views.index, name='index'),
]
