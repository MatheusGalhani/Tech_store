# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id_contato', models.AutoField(primary_key=True, serialize=False)),
                ('nome_contato', models.CharField(max_length=200)),
                ('email_contato', models.EmailField(max_length=250)),
                ('data_nascimento', models.DateField()),
                ('telefone_contato', models.IntegerField()),
                ('cpf_contato', models.IntegerField()),
                ('estado', models.CharField(max_length=200, choices=[('acre', 'Acre'), ('alagoas', 'Alagoas'), ('amapá', 'Amapá'), ('amazonas', 'Amazonas'), ('bahia', 'Bahia'), ('ceará', 'Ceará'), ('distrito federal', 'Distrito Federal'), ('espírito santo', 'Espírito Santo'), ('goiás', 'Goiás'), ('maranhão', 'Maranhão'), ('mato grosso', 'Mato Grosso'), ('mato grosso do sul', 'Mato Grosso do Sul'), ('minas gerais', 'Minas Gerais'), ('pará', 'Pará'), ('paraíba', 'Paraíba'), ('paraná', 'Paraná'), ('pernambuco', 'Pernambuco'), ('piauí', 'Piauí'), ('rio de janeiro', 'Rio de Janeiro'), ('rio grande do norte', 'Rio Grande do Norte'), ('rio grande do sul', 'Rio Grande do Sul'), ('rondônia', 'Rondônia'), ('roraima', 'Roraima'), ('santa catarina', 'Santa Catarina'), ('são paulo', 'São Paulo'), ('sergipe', 'Sergipe'), ('tocantins', 'Tocantins')])),
                ('cidade', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=160)),
                ('descricao_produto', models.TextField()),
                ('preco_produto', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qntd_produto', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
