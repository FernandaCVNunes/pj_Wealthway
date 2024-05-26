from django import forms
from .models import Financas


class FinancasForm(forms.ModelForm):
    class Meta:
        model = Financas
        fields = ['nome_meta', 'descricao', 'valor_total', 'valor_mensal', 'parcelas_totais']
        descricao = forms.CharField(widget=forms.Textarea)
        widgets = {
            'parcelas_totais': forms.HiddenInput(),
        }

    def clean_nome_meta(self):
        nome_meta = self.cleaned_data.get('nome_meta')
        if not nome_meta:
            raise forms.ValidationError('Este campo é obrigatório.')
        if Financas.objects.filter(nome_meta=nome_meta).exists():
            raise forms.ValidationError('Nome da meta já existe.')
        return nome_meta

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if not descricao:
            raise forms.ValidationError('Este campo é obrigatório.')
        if Financas.objects.filter(descricao=descricao).exists():
            raise forms.ValidationError('Descrição já existe.')
        return descricao

    def clean_valor_total(self):
        valor_total = self.cleaned_data.get('valor_total')
        if not valor_total:
            raise forms.ValidationError('Este campo é obrigatório.')
        if valor_total ==0:
            raise forms.ValidationError('O valor total não pode ser zero.')
        return valor_total

    def clean_valor_mensal(self):
        valor_mensal = self.cleaned_data.get('valor_mensal')
        if not valor_mensal:
            raise forms.ValidationError('Este campo é obrigatório.')
        if valor_mensal ==0:
            raise forms.ValidationError('O valor mensal não pode ser zero.')
        return valor_mensal