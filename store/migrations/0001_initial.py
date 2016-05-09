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
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=160)),
                ('descricao_produto', models.TextField()),
                ('imagem_produto', models.FileField(verbose_name='Foto do produto', upload_to='', null=True)),
                ('categoria_produto', models.CharField(verbose_name='Categoria', max_length=200, choices=[('adaptador', 'Adaptador'), ('desktop', 'Desktop'), ('hardware', 'Hardware'), ('impressora', 'Impressora'), ('mouse', 'Mouse'), ('notebook', 'Notebook'), ('perifericos', 'Periféricos'), ('smartphone', 'Smartphone'), ('tablet', 'Tablet'), ('teclado', 'Teclado'), ('televisao', 'Televisão')])),
                ('preco_produto', models.DecimalField(verbose_name='Preço do produto', max_digits=15, decimal_places=2)),
                ('qntd_produto', models.IntegerField(verbose_name='Quantidade de estoque')),
            ],
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
