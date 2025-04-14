from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Administracao.models import SetoresCad
from .forms import CadServicosForm, CadLocaisForm
from .models import ServicosCad

# CONFIGURAÇÕES ==============================================================================================
class ConfiguracoesView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "Configuracoes/configuracoes.html"
    
    
    
#Gerenciar Serviços ==========================================================================================
class gerenciar_servicos(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'Configuracoes/configuracoes-gerenciar_servicos.html'    
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        setor = user.setores.first()        

        servicos = ServicosCad.objects.filter(setores=setor)
        FormCadServico = CadServicosForm
        
        context = {
            'servicos': servicos, #Passa os registros
            'FomCadServico': FormCadServico #Passa o form vazio
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        if "deletar" in request.POST:
            return self.deletar(request)
        else:
            return self.cadastrar_editar(request)
    
    def deletar(self, request):
        id_servico = request.POST.get("deletar")
        servico = get_object_or_404(ServicosCad, id=id_servico)
        servico.delete()
        return JsonResponse({"status": "success"})
        
    def cadastrar_editar(self, request, *args, **kwargs):
        servico_id = request.POST.get("servico_id")

        if servico_id:
            servico = get_object_or_404(ServicosCad, id=servico_id)
            form = CadServicosForm(request.POST, instance=servico)
        else:
            form = CadServicosForm(request.POST)

        if form.is_valid():
            servico = form.save(commit=False)
            setor = request.user.setores.first()
            servico.save()
            servico.setores.add(setor)

            if servico_id:
                return JsonResponse({
                    "status": "success",
                    "message": "Serviço atualizado com sucesso!"
                })
            else:
                return JsonResponse({
                    "status": "success",
                    "message": "Serviço cadastrado com sucesso!"
                })

        return JsonResponse({
            "status": "error",
            "message": "Erro ao salvar serviço!",
            "errors": form.errors
        }, status=400)

def listar_servicos_json(request):
    user = request.user
    setor = user.setores.first()
    servicos = ServicosCad.objects.filter(setores=setor).values("sigla", nome=F("N_Servico"))

    return JsonResponse({
        "servicos": list(servicos)
    })
    
#Locais
class gerenciar_locais(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'Configuracoes/configuracoes-gerenciar_locais.html'
    
#Senhas
class gerenciar_senhas(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'Configuracoes/configuracoes-gerenciar_senhas.html'