# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='cidade',
            new_name='contato_cidade',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='email',
            new_name='contato_email',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='endereco',
            new_name='contato_endereco',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='estado',
            new_name='contato_estado',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='nome_contato',
            new_name='contato_nome',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='cpf',
            new_name='cpf_contato',
        ),
    ]
