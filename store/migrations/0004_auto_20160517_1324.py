# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20160511_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem_produto',
            field=models.FileField(verbose_name='Foto do produto', upload_to=''),
        ),
    ]
