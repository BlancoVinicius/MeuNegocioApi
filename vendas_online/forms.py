from allauth.account.forms import SignupForm, LoginForm


class CustomSignupForm(SignupForm):

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        # Adicionando classes CSS personalizadas aos campos
        self.fields['username'].widget.attrs.update({"class":"form-control"})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['password1'].widget
        


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        # Adicionando classes CSS personalizadas aos campos
        self.fields['login'].widget.attrs.update({"class":"form-control"})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
       