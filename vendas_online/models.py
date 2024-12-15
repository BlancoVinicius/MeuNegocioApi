from django.db import models

# Create your models here.

from django import forms

class FormCadastro(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    senha = forms.PasswordInput()
