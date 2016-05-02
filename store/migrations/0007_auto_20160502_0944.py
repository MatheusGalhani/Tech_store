# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20160502_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='contato_cidade',
            field=models.CharField(max_length=200, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='contato_email',
            field=models.EmailField(unique=True, max_length=250, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='contato_endereco',
            field=models.CharField(max_length=400, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='contato_estado',
            field=models.CharField(max_length=200, choices=[('acre', 'Acre'), ('alagoas', 'Alagoas'), ('amapá', 'Amapá'), ('amazonas', 'Amazonas'), ('bahia', 'Bahia'), ('ceará', 'Ceará'), ('distrito federal', 'Distrito Federal'), ('espírito santo', 'Espírito Santo'), ('goiás', 'Goiás'), ('maranhão', 'Maranhão'), ('mato grosso', 'Mato Grosso'), ('mato grosso do sul', 'Mato Grosso do Sul'), ('minas gerais', 'Minas Gerais'), ('pará', 'Pará'), ('paraíba', 'Paraíba'), ('paraná', 'Paraná'), ('pernambuco', 'Pernambuco'), ('piauí', 'Piauí'), ('rio de janeiro', 'Rio de Janeiro'), ('rio grande do norte', 'Rio Grande do Norte'), ('rio grande do sul', 'Rio Grande do Sul'), ('rondônia', 'Rondônia'), ('roraima', 'Roraima'), ('santa catarina', 'Santa Catarina'), ('são paulo', 'São Paulo'), ('sergipe', 'Sergipe'), ('tocantins', 'Tocantins')], verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='contato_nome',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='cpf_contato',
            field=models.CharField(unique=True, max_length=30, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria_produto',
            field=models.CharField(max_length=200, choices=[('adaptador', 'Adaptador'), ('desktop', 'Desktop'), ('hardware', 'Hardware'), ('impressora', 'Impressora'), ('mouse', 'Mouse'), ('notebook', 'Notebook'), ('perifericos', 'Periféricos'), ('smartphone', 'Smartphone'), ('tablet', 'Tablet'), ('teclado', 'Teclado'), ('televisao', 'Televisão')], verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem_produto',
            field=models.FileField(null=True, blank=True, upload_to='', verbose_name='Foto do produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_produto',
            field=models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Preço do produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qntd_produto',
            field=models.IntegerField(verbose_name='Quantidade de estoque'),
        ),
    ]
