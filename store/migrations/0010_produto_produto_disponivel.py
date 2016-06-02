# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20160602_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='produto_disponivel',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
    ]
