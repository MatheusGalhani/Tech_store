# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_produto_produto_disponivel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='produto_disponivel',
            new_name='produto_indisponivel',
        ),
    ]
