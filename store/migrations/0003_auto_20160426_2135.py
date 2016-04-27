# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160426_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='cpf_contato',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='email_contato',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='nome_contato',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='telefone_contato',
            new_name='telefone_de_contato',
        ),
    ]
