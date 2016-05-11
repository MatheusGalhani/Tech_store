# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='cep_endereco',
            field=models.CharField(max_length=50, verbose_name='CEP', validators=[store.models.validate_cep]),
        ),
        migrations.AlterField(
            model_name='contato',
            name='complemento_endereco',
            field=models.CharField(null=True, max_length=400, verbose_name='Complemento', blank=True),
        ),
    ]
