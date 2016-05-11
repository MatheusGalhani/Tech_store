from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from store.base import CPF, CEP

#My choices
ESTADO_CHOICES = (
	(u'acre', u'Acre'),
	(u'amapa', u'Amapá'),
	(u'alagoas', u'Alagoas'),
	(u'amazonas', u'Amazonas'),
	(u'bahia', u'Bahia'),
	(u'ceara', u'Ceará'),
	(u'distrito federal', u'Distrito Federal'),
	(u'espirito santo', u'Espírito Santo'),
	(u'goias', u'Goiás'),
	(u'maranhao', u'Maranhão'),
	(u'mato grosso', u'Mato Grosso'),
	(u'mato grosso do sul', u'Mato Grosso do Sul'),
	(u'minas gerais', u'Minas Gerais'),
	(u'para', u'Pará'),
	(u'paraiba', u'Paraíba'),
	(u'parana', u'Paraná'),
	(u'pernambuco', u'Pernambuco'),
	(u'piaui', u'Piauí'),
	(u'rio de janeiro', u'Rio de Janeiro'),
	(u'rio grande do sul', u'Rio Grande do Norte'),
	(u'rio grande do sul', u'Rio Grande do Sul'),
	(u'rondonia', u'Rondônia'),
	(u'roraima', u'Roraima'),
	(u'santa catarina', u'Santa Catarina'),
	(u'sao paulo', u'São Paulo'),
	(u'sergipe', u'Sergipe'),
	(u'tocantins', u'Tocantins'),
)

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

#My Validator
def validate_cpf(value):
    if not CPF.validate(value):
        raise ValidationError(
            _('%(value)s is not a valid CPF "EXAMPLE: 123.456.789-11"'),
            params={'value': value},
        )

def validate_cep(value):
    if not CEP.validate(value):
        raise ValidationError(
            _('%(value)s is not a valid CEP "EXAMPLE: 14810-142"'),
            params={'value': value},
        )


# Create your models here.
class Produto(models.Model):
	id_produto = models.AutoField(primary_key=True)
	nome_produto = models.CharField(max_length=160)
	descricao_produto = models.TextField()
	imagem_produto = models.FileField(null=True, verbose_name=u'Foto do produto')
	categoria_produto = models.CharField(choices= CATEGORIA_CHOICES, max_length=200, verbose_name=u'Categoria')
	preco_produto = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=u'Preço da venda')
	qntd_produto = models.IntegerField(verbose_name=u'Quantidade de estoque')
	valor_compra = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=u'Preço da compra')
	def __str__(self):
		return self.nome_produto

class Pagamento(models.Model):
	id_pagamento = models.AutoField(primary_key=True)
	tipo_pagamento = models.CharField(max_length=160, unique=True)
	def __str__(self):
		return self.tipo_pagamento

class Statu(models.Model):
	id_status = models.AutoField(primary_key=True)
	status_info = models.CharField(max_length=160, unique=True, verbose_name=u'Status')
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

class Contato(models.Model):
	id_contato = models.AutoField(primary_key=True)
	author_usuario = models.ForeignKey('auth.User', verbose_name=u'Usuario', unique=True,)
	nome_completo = models.CharField(max_length=260)
	cpf_contato = models.CharField(unique=True, verbose_name=u'CPF', max_length=14, validators=[validate_cpf])
	telefone_contato = models.CharField(max_length=60)
	email_contato = models.EmailField(max_length = 100, unique=True, verbose_name=u'EMAIL')
	data_nascimento = models.DateField()
	estado_pais =  models.CharField(choices= ESTADO_CHOICES, max_length=200, verbose_name=u'Estado')
	cidade_estado = models.CharField(max_length=200, verbose_name=u'Cidade')
	endereco_completo = models.CharField(max_length=400, verbose_name=u'Endereço Completo')
	numero_casa = models.IntegerField(verbose_name=u'Número')
	bairro_endereco = models.CharField(max_length=400, verbose_name=u'Bairro')
	complemento_endereco = models.CharField(blank=True,null=True, max_length=400, verbose_name=u'Complemento')
	cep_endereco = models.CharField(max_length=50, verbose_name=u'CEP', validators=[validate_cep])
	def __str__(self):
		return self.cpf_contato