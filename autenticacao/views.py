from django.shortcuts import render, redirect
from django.views.generic import View 
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.

class CadastroView(View):
    def get(self, request):
        form = NewUserForm()
        return render(request, 'autenticacao/cadastro.html', context={"register_form":form})
    
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('home')
        messages.error(request, "Erro de registração. Informação invalida.")
        return render(request=request, template_name='autenticacao/cadastro.html', context={"register_form": form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name="autenticacao/login.html", context={"login_form":form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"VOcê agora está conectado como {username}.")
                return redirect("home")
            else:
                messages.error(request,"Usuario ou senha invalido")
        else:
            messages.error(request,"Usuario invalido")

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Você está desconectado")
        return redirect("home")
