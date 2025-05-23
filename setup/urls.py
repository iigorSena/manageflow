from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView


from Home.views import LoginView, LogoutView, HomeView
from Triagem.views import TriagemView
from Configuracoes.views import ConfiguracoesView, gerenciar_servicos, listar_servicos_json, gerenciar_locais, listar_locais_json, gerenciar_senhas

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    
    path('triagem/', TriagemView.as_view(), name='triagem'),
    
    path('configuracoes/', ConfiguracoesView.as_view(), name="configuracoes"),
    path('gerenciar-servicos/', gerenciar_servicos.as_view(), name='gerenciar_servicos'),
    path("listar-servicos-json/", listar_servicos_json, name="listar_servicos_json"),
    
    path('gerenciar-locais/', gerenciar_locais.as_view(), name='gerenciar_locais'),
    path("listar-locais-json/", listar_locais_json, name="listar_locais_json"),

    path('gerenciar-senhas/', gerenciar_senhas.as_view(), name='gerenciar_senhas'),
]
