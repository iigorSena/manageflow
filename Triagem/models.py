from django.db import models
from django.utils import timezone

from Configuracoes.models import ServicosCad

class SenhasCad(models.Model):
    servico = models.ForeignKey(ServicosCad, on_delete=models.CASCADE, related_name='Serviço')
    numero = models.PositiveIntegerField()  # número sequencial por serviço
    codigo = models.CharField(max_length=10)  # ex: TRI001
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_emissao = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('servico', 'numero')  # evitar duplicidade por dia
        ordering = ['-data_emissao']

    def __str__(self):
        return f"{self.codigo} - {self.servico}"
