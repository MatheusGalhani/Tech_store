# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_produto_data_publicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='data_publicacao',
        ),
    ]
