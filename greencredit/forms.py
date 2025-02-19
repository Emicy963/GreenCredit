from django import forms
from .models import Produto, Credito, Compra, ItemCompra, Pagamento
from django.forms import inlineformset_factory

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
    
class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        exclude = ['cliente', 'status', 'data_aprovacao', 'valor_aprovado']
        widgets = {
            'data_solicitacao': forms.DateInput(attrs={'type': 'date'})
        }

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        exclude = ['cliente', 'data_compra', 'valor_total']

class ItemCompraForm(forms.ModelForm):
    class Meta:
        model = ItemCompra
        fields = ['produto', 'quantidade']

ItemCompraFormSet = inlineformset_factory(
    Compra,
    ItemCompra,
    form=ItemCompraForm,
    extra=1,
    can_delete=False
)

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['valor', 'forma_pagamento', 'comprovante']
