from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView

from Administracao.models import SetoresCad

class LoginView(TemplateView):
    template_name = "Home/login.html"

    def get(self, request, *args, **kwargs):
        login_form = AuthenticationForm()
        return render(request, self.template_name, {'login_form': login_form})

    def post(self, request, *args, **kwargs):
        login_form = AuthenticationForm(request, data=request.POST)
        message_error = None  # Inicializa a variável

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message_error = "Usuário ou senha inválidos."  # Define o erro ao falhar o login

        return render(request, self.template_name, {'login_form': login_form, 'message_error': message_error})

def LogoutView(resquest):
    logout(resquest)
    return redirect('login')

class HomeView(TemplateView):
    template_name = 'Home/home.html'
    
def setor_usuario(request):
    setor = request.user.setores.first()  # Pega o primeiro setor do usuário
    return render(request, 'Home/modelo.html', {'setor': setor})

