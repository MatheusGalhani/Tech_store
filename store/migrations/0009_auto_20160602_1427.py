# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20160602_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='id_compra',
            field=models.CharField(verbose_name='Numero Pedido', max_length=10000),
        ),
    ]
