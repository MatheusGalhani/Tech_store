# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


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
                ('preco_total', models.DecimalField(verbose_name='Preço Total', decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id_pagamento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_pagamento', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=160)),
                ('descricao_produto', models.TextField()),
                ('imagem_produto', models.FileField(null=True, verbose_name='Foto do produto', upload_to='')),
                ('categoria_produto', models.CharField(max_length=200, verbose_name='Categoria', choices=[('cameras', 'Câmeras Digitais'), ('desktop', 'Desktop'), ('hardware', 'Hardware'), ('impressora', 'Impressora'), ('notebook', 'Notebook'), ('perifericos', 'Periféricos'), ('redes', 'Redes'), ('smartphone', 'Smartphone'), ('software', 'Software'), ('tablet', 'Tablet'), ('televisao', 'Televisão')])),
                ('preco_produto', models.DecimalField(verbose_name='Preço do produto', decimal_places=2, max_digits=15)),
                ('qntd_produto', models.IntegerField(verbose_name='Quantidade de estoque')),
            ],
        ),
        migrations.CreateModel(
            name='Statu',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('status_info', models.CharField(max_length=160, verbose_name='Status')),
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
