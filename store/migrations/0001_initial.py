# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id_carrinho', models.AutoField(primary_key=True, serialize=False)),
                ('qntd_produtos', models.IntegerField(verbose_name='Quantidade de produtos')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('preco_total', models.DecimalField(decimal_places=2, verbose_name='Preço Total', max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id_contato', models.AutoField(primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=260)),
                ('cpf_contato', models.CharField(unique=True, max_length=50, verbose_name='CPF')),
                ('telefone_contato', models.CharField(max_length=60)),
                ('email_contato', models.CharField(unique=True, max_length=100, verbose_name='EMAIL')),
                ('data_nascimento', models.DateField()),
                ('estado_pais', models.CharField(max_length=200, verbose_name='Estado', choices=[('acre', 'Acre'), ('amapa', 'Amapá'), ('alagoas', 'Alagoas'), ('amazonas', 'Amazonas'), ('bahia', 'Bahia'), ('ceara', 'Ceará'), ('distrito federal', 'Distrito Federal'), ('espirito santo', 'Espírito Santo'), ('goias', 'Goiás'), ('maranhao', 'Maranhão'), ('mato grosso', 'Mato Grosso'), ('mato grosso do sul', 'Mato Grosso do Sul'), ('minas gerais', 'Minas Gerais'), ('para', 'Pará'), ('paraiba', 'Paraíba'), ('parana', 'Paraná'), ('pernambuco', 'Pernambuco'), ('piaui', 'Piauí'), ('rio de janeiro', 'Rio de Janeiro'), ('rio grande do sul', 'Rio Grande do Norte'), ('rio grande do sul', 'Rio Grande do Sul'), ('rondonia', 'Rondônia'), ('roraima', 'Roraima'), ('santa catarina', 'Santa Catarina'), ('sao paulo', 'São Paulo'), ('sergipe', 'Sergipe'), ('tocantins', 'Tocantins')])),
                ('cidade_estado', models.CharField(max_length=200, verbose_name='Cidade')),
                ('endereco_completo', models.CharField(max_length=400, verbose_name='Endereço Completo')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id_pagamento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_pagamento', models.CharField(unique=True, max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=160)),
                ('descricao_produto', models.TextField()),
                ('imagem_produto', models.FileField(verbose_name='Foto do produto', upload_to='', null=True)),
                ('categoria_produto', models.CharField(max_length=200, verbose_name='Categoria', choices=[('cameras', 'Câmeras Digitais'), ('desktop', 'Desktop'), ('hardware', 'Hardware'), ('impressora', 'Impressora'), ('notebook', 'Notebook'), ('perifericos', 'Periféricos'), ('redes', 'Redes'), ('smartphone', 'Smartphone'), ('software', 'Software'), ('tablet', 'Tablet'), ('televisao', 'Televisão')])),
                ('preco_produto', models.DecimalField(decimal_places=2, verbose_name='Preço da venda', max_digits=15)),
                ('qntd_produto', models.IntegerField(verbose_name='Quantidade de estoque')),
                ('valor_compra', models.DecimalField(decimal_places=2, verbose_name='Preço da compra', max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Statu',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('status_info', models.CharField(unique=True, max_length=160, verbose_name='Status')),
            ],
        ),
        migrations.AddField(
            model_name='carrinho',
            name='id_status',
            field=models.ForeignKey(to='store.Statu'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='id_tipo_pagamento',
            field=models.ForeignKey(to='store.Pagamento'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produto_compra',
            field=models.ForeignKey(to='store.Produto'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='usuario_compra',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
