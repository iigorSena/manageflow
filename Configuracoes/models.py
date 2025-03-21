from django.db import models

from Administracao.models import SetoresCad
class ServicosCad(models.Model):
    class StatusChoicesServico(models.TextChoices):
        ATIVO = 'Ativo', 'Ativo'
        INATIVO = 'Inativo', 'Inativo'
        
    sigla = models.CharField(max_length=3, verbose_name="Sigla")
    N_Servico = models.CharField(max_length=50, verbose_name="Serviços")
    status = models.CharField(max_length=8, choices=StatusChoicesServico.choices, default=StatusChoicesServico.ATIVO)
    
    servicos = models.ManyToManyField(SetoresCad, related_name="Servico_Setores")
    
    def __str__(self):
        return self.N_Servico