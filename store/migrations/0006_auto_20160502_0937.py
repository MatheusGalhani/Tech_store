# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160502_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='contato_email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='contato_nome',
            field=models.CharField(max_length=200),
        ),
    ]
