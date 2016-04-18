from django.db import models
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    descricao_produto = models.TextField()
    preco_produto = models.DecimalField(max_digits=15, decimal_places=2)
    qntd_produto = models.IntegerField()

def __str__(self):
        return self.nome_produto
