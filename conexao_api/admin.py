from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.models import UserToken

class UserTokenAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'access_token', 'refresh_token', 'user_id_api')
    
    # Campos que podem ser usados para buscar registros
    search_fields = ('user__username', 'access_token')

    # Permite filtrar os resultados
    list_filter = ('user',)

# Registrando o modelo UserToken com a classe personalizada
admin.site.register(UserToken, UserTokenAdmin)
