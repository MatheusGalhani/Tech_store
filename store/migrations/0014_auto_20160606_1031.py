# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20160605_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='id_contato',
            field=models.AutoField(serialize=False, verbose_name='Código do Cliente', primary_key=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='id_produto',
            field=models.AutoField(serialize=False, verbose_name='Código do Produto', primary_key=True),
        ),
    ]
