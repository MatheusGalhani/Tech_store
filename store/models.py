from django.db import models
from django.utils import timezone

#My choices
CATEGORIA_CHOICES = (
	(u'cameras', u'Câmeras Digitais'),
	(u'desktop', u'Desktop'),
	(u'hardware', u'Hardware'),
	(u'impressora', u'Impressora'),
	(u'notebook', u'Notebook'),
	(u'perifericos', u'Periféricos'),
	(u'redes', u'Redes'),
	(u'smartphone', u'Smartphone'),
	(u'software', u'Software'),
	(u'tablet', u'Tablet'),
	(u'televisao', u'Televisão'),
)


# Create your models here.
class Produto(models.Model):
	id_produto = models.AutoField(primary_key=True)
	nome_produto = models.CharField(max_length=160)
	descricao_produto = models.TextField()
	imagem_produto = models.FileField(null=True, verbose_name=u'Foto do produto')
	categoria_produto = models.CharField(choices= CATEGORIA_CHOICES, max_length=200, verbose_name=u'Categoria')
	preco_produto = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=u'Preço do produto')
	qntd_produto = models.IntegerField(verbose_name=u'Quantidade de estoque')
	def __str__(self):
		return self.nome_produto

class Pagamento(models.Model):
	id_pagamento = models.AutoField(primary_key=True)
	tipo_pagamento = models.CharField(max_length=160)
	def __str__(self):
		return self.tipo_pagamento

class Statu(models.Model):
	id_status = models.AutoField(primary_key=True)
	status_info = models.CharField(max_length=160, verbose_name=u'Status')
	def __str__(self):
		return self.status_info

class Carrinho(models.Model):
	id_carrinho = models.AutoField(primary_key=True)
	usuario_compra = models.ForeignKey('auth.User')
	qntd_produtos = models.IntegerField(verbose_name=u'Quantidade de produtos')
	created_date = models.DateTimeField(default=timezone.now)
	produto_compra = models.ForeignKey('Produto')
	preco_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=u'Preço Total')
	id_tipo_pagamento = models.ForeignKey('Pagamento')
	id_status = models.ForeignKey('Statu')
	def __str__(self):
		return self.usuario_compra