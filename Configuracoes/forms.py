from django import forms

from Administracao.models import SetoresCad
from .models import ServicosCad, LocaisCad

class CadServicosForm(forms.ModelForm):
    class Meta:
        model = ServicosCad
        fields = ["sigla", "N_Servico", "status"]
        
    status = forms.ChoiceField(choices=ServicosCad.StatusChoicesServico.choices, initial=ServicosCad.StatusChoicesServico.ATIVO, required=False)

class CadLocaisForm(forms.ModelForm):
    class Meta:
        model = LocaisCad
        fields = ["N_Local", "status"]
        
    status = forms.ChoiceField(choices=ServicosCad.StatusChoicesServico.choices, initial=ServicosCad.StatusChoicesServico.ATIVO, required=False)
