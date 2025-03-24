from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CadServicosForm, CadLocaisForm
from .models import ServicosCad

# CONFIGURAÇÕES ==============================================================================================
class ConfiguracoesView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "Configuracoes/configuracoes.html"
    
#Gerenciar Serviços
class gerenciar_servicos(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'Configuracoes/configuracoes-gerenciar_servicos.html'
    
    def get(self, request, *args, **kwargs):
        form = CadServicosForm() #Passa o form vazio
        servicos = ServicosCad.objects.all() #Passa os registros
        
        return render(request, self.template_name, {"FomCadServico": form, "servico": servicos})
    
    def post(self, request, *args, **kwargs):
        form = CadServicosForm(request.POST)
        print(form)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.save()
            return JsonResponse({"status": "Serviço cadastrado com Sucesso"}, status=200)
        return JsonResponse({"status": "error", "message": "Ocorreu um erro ao realizar o cadastro."}, status=400)
    
#Locais
class gerenciar_locais(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'Configuracoes/configuracoes-gerenciar_locais.html'
    
#Senhas
class gerenciar_senhas(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'Configuracoes/configuracoes-gerenciar_senhas.html'