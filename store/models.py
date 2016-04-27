from django.db import models
from django.utils import timezone

	#My choices
ESTADO_CHOICES = (
	(u'acre', u'Acre'),
	(u'alagoas', u'Alagoas'),
	(u'amapá',u'Amapá'),
	(u'amazonas', u'Amazonas'),
	(u'bahia', u'Bahia'),
	(u'ceará', u'Ceará'),
	(u'distrito federal', u'Distrito Federal'),
	(u'espírito santo', u'Espírito Santo'),
	(u'goiás', u'Goiás'),
	(u'maranhão', u'Maranhão'),
	(u'mato grosso', u'Mato Grosso'),
	(u'mato grosso do sul', u'Mato Grosso do Sul'),
	(u'minas gerais', u'Minas Gerais'),
	(u'pará', u'Pará'),
	(u'paraíba', u'Paraíba'),
	(u'paraná', u'Paraná'),
	(u'pernambuco', u'Pernambuco'),
	(u'piauí', u'Piauí'),
	(u'rio de janeiro', u'Rio de Janeiro'),
	(u'rio grande do norte', u'Rio Grande do Norte'),
	(u'rio grande do sul', u'Rio Grande do Sul'),
	(u'rondônia', u'Rondônia'),
	(u'roraima', u'Roraima'),
	(u'santa catarina', u'Santa Catarina'),
	(u'são paulo', u'São Paulo'),
	(u'sergipe', u'Sergipe'),
	(u'tocantins', u'Tocantins'),
)

# Create your models here.
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=160)
    descricao_produto = models.TextField()
    preco_produto = models.DecimalField(max_digits=15, decimal_places=2)
    qntd_produto = models.IntegerField()


def __str__(self):
    return self.nome_produto

class Contato(models.Model):
	id_contato = models.AutoField(primary_key=True)
	nome_completo = models.CharField(max_length=200)
	email = models.EmailField(max_length=250)
	data_nascimento = models.DateField()
	telefone_de_contato = models.IntegerField()
	cpf = models.IntegerField()
	estado = models.CharField(choices= ESTADO_CHOICES, max_length=200)
	cidade = models.CharField(max_length=200)
	endereco = models.CharField(max_length=400)

def __str__(self):
    return self.nome_contato
