# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20160528_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='id_compra',
            field=models.CharField(max_length=10000, verbose_name='Numero Pedido', default=''),
            preserve_default=False,
        ),
    ]
