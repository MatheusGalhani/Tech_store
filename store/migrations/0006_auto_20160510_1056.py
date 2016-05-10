# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160510_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='author_usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email_contato',
            field=models.EmailField(max_length=100, unique=True, verbose_name='EMAIL'),
        ),
    ]
