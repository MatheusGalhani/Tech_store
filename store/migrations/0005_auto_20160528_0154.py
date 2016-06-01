# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20160517_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='id_tipo_pagamento',
        ),
        migrations.DeleteModel(
            name='Pagamento',
        ),
    ]
