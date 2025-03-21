from django.contrib import admin
from django.urls import path

from Home.views import LoginView, LogoutView, HomeView
from Configuracoes.views import ConfiguracoesView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    
    path('configuracoes/', ConfiguracoesView.as_view(), name='configuracoes'),

]
