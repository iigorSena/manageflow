from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CadServico
class ConfiguracoesView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "Configuracoes/configuracoes.html"
    

    def novo_servico(self, request):
        if request.method == "POST":
            form = CadServico(request.POST)
            if form.is_valid():
                form.save()  # Salva o novo serviço no banco de dados
                return JsonResponse({'success': True})  # Retorna sucesso via AJAX
            return JsonResponse({'success': False, 'errors': form.errors})  # Retorna erros do formulário

        # Chama o Cadastro do Serviço
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = CadServico()
            return render(request, "Configuracoes/configuracoes_novo_servico.html", {"FomCadServico":form})

        return JsonResponse({'error': 'Requisição inválida'}, status=400)

