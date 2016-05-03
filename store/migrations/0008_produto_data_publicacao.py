# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20160502_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
