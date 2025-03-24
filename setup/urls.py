from django.contrib import admin
from django.urls import path

from Home.views import LoginView, LogoutView, HomeView
from Configuracoes.views import ConfiguracoesView, gerenciar_servicos, gerenciar_locais, gerenciar_senhas

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    
    path('configuracoes/', ConfiguracoesView.as_view(), name='configuracoes'),
    path('gerenciar-servicos/', gerenciar_servicos.as_view(), name='gerenciar_servicos'),
    path('gerenciar-locais/', gerenciar_locais.as_view(), name='gerenciar_locais'),
    path('gerenciar-senhas/', gerenciar_senhas.as_view(), name='gerenciar_senhas'),
]
