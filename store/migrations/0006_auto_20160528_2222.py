# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160528_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(unique=True, max_length=160),
        ),
    ]
