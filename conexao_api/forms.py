from django import forms
from conexao_api.models.anuncio import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = '__all__'

