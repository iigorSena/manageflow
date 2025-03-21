from django import forms

from Administracao.models import SetoresCad
from .models import ServicosCad

class CadServico(forms.ModelForm):
    class Meta:
        model = ServicosCad
        fields = ["sigla", "N_Servico", "status"]