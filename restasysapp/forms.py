from django import forms
from .models import Mesa, Pratos, Pedidos, Pedidos_Fechados

class MesaForm(forms.ModelForm):

    class Meta:
        model = Mesa
        fields = ('numero',)

class PratosForm(forms.ModelForm):

    class Meta:
        model = Pratos
        fields = ('nome', 'valor', 'ingredientes')

class PedidosForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ('mesa_id', 'pratos_id', 'valor_total')
