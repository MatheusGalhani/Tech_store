# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_produto_categoria_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='contato_nome',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='cpf_contato',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone_de_contato',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria_produto',
            field=models.CharField(max_length=200, choices=[('adaptador', 'Adaptador'), ('desktop', 'Desktop'), ('hardware', 'Hardware'), ('impressora', 'Impressora'), ('mouse', 'Mouse'), ('notebook', 'Notebook'), ('perifericos', 'Periféricos'), ('smartphone', 'Smartphone'), ('tablet', 'Tablet'), ('teclado', 'Teclado'), ('televisao', 'Televisão')]),
        ),
    ]
