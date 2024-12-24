from allauth.account.forms import SignupForm, LoginForm
from django import forms

from django.contrib.auth.models import User
class CustomSignupForm(SignupForm):

    # username = forms.CharField(
    #     label="Username",
    #     min_length=3,
    #     widget=forms.TextInput(
    #         attrs={"placeholder": "Username", "autocomplete": "username"}
    #     ),
    # )

    # email = forms.EmailField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "type": "email",
    #             "placeholder": "Email address",
    #             "autocomplete": "email",
    #         }
    #     )
    # )

    first_name = forms.CharField(
        max_length=30,
        label='Nome', 
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length=30,
        label='Sobrenome', 
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adicionando classes CSS personalizadas aos campos
        self.fields['username'].widget.attrs.update({"class":"form-control"})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        
        # help_text_password1 = """
        #     <ul>
        #     <li>Sua senha não pode ser muito parecida com o resto das suas informações pessoais.</li>
        #     <li>Sua senha deve conter ao menos 8 caracteres.</li>
        #     <li>Sua senha não pode ser uma senha comum.</li>
        #     <li>Sua senha não pode ser inteiramente numérica.</li>
        #     </ul>
        # """
        
        # self.fields['password1'].help_text = help_text_password1
        


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        # Adicionando classes CSS personalizadas aos campos
        self.fields['login'].widget.attrs.update({"class":"form-control"})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
       