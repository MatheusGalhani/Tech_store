# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_produto_imagem_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria_produto',
            field=models.CharField(choices=[('adaptador', 'Adaptador'), ('desktop', 'Desktop'), ('hardware', 'Hardware'), ('impressora', 'Impressora'), ('mouse', 'Mouse'), ('notebook', 'Notebook'), ('perifericos', 'Periféricos'), ('smartphone', 'Smartphone'), ('tablet', 'Tablet'), ('teclado', 'Teclado')], default='', max_length=200),
            preserve_default=False,
        ),
    ]
