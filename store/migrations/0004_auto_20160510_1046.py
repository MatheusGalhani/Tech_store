# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20160510_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='author',
            new_name='author_usuario',
        ),
    ]
