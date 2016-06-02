# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_carrinho_id_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='id_compra',
            field=models.IntegerField(verbose_name='Numero Pedido'),
        ),
    ]
