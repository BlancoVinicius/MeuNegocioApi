from django.urls import path
from vendas_online import views

app_name = 'vendas_online'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),


    
    # path('teste/', views.teste, name='teste'),
    # path('teste/<int:id>/', views.teste, name='teste'),
]
