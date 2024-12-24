from django.shortcuts import redirect, render
from vendas_online.forms import CustomSignupForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'templates_vendas_onlina/entrada.html')

def login(request):
    return redirect('/accounts/login/')
    # return render(request, 'templates_vendas_onlina/login.html')

@login_required
def home(request):
    
    # if request.method == 'POST':
    #     form = CustomSignupForm(request.POST)
    #     if form.is_valid():
    #         form.save(request)
    #         return redirect('/login/')
    #     elif not form.is_valid():
            
    #         return render(request, 'account/signup.html', {'form': form})

    # form = CustomSignupForm()

    return render(
        request, 'templates_vendas_onlina/home.html',
        # {'form': form}
    )