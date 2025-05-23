from django.shortcuts import render
from django.views import View
from django.urls import reverse, reverse_lazy
from django.db.models import Count
from django.utils.timezone import now
from django.contrib.auth.mixins import LoginRequiredMixin


from Triagem.models import SenhasCad
from Configuracoes.models import ServicosCad, SetoresCad


class TriagemView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = "Triagem/Triagem.html"
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        print(f'O usuário logado é: ', user)
        setor = user.setores.first()
        print(f'O setor do usuário logado é: ', setor)
        hoje = now().date()

        # Busca todos os serviços
        servicos = ServicosCad.objects.filter(setores=setor, status="Ativo")
        print(f'O serviços registrados são: ', servicos)

        # Conta quantas senhas foram emitidas hoje por serviço
        contagem_senhas = (
            SenhasCad.objects
            .filter(data_emissao__date=hoje)
            .values('servico')
            .annotate(total=Count('id'))
        )
        print(f'Contagem de senhas emitidas hoje: ', contagem_senhas)

        # Cria um dicionário com {servico_id: total}
        totais_por_servico = {item['servico']: item['total'] for item in contagem_senhas}
        print(f'Totais por serviço: ', totais_por_servico)


        # Junta os serviços com seus totais (ou 0 se não houver)
        servicos_com_totais = []
        for servico in servicos:
            total = totais_por_servico.get(servico.id, 0)
            print(f"Serviço: {servico.N_Servico}, Total de senhas: {total}")
            servicos_com_totais.append({
                'servico': servico,
                'total': total
            })
        print(f'Os serviços são: ', servico)
        print(f'Os totais são: ', total)

        context = {
            'servicos_com_totais': servicos_com_totais
        }
        print(f'O resultados esperados é: ', servicos_com_totais)

        print('Renderizando com contexto:', context)
        return render(request, self.template_name)