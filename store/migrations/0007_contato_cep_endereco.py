# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20160510_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='cep_endereco',
            field=models.CharField(max_length=50, verbose_name='CEP', default=''),
            preserve_default=False,
        ),
    ]
