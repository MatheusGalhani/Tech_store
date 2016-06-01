from django import forms
from .models import Carrinho

class CarrinhoForm(forms.ModelForm):
	class Meta:
		model = Carrinho
		fields = ('usuario_compra', 'qntd_produtos', 'produto_compra', 'preco_total', 'id_status')
