# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160427_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem_produto',
            field=models.FileField(null=True, upload_to='', blank=True),
        ),
    ]
