# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20160603_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='numero_casa',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Número'),
        ),
    ]
