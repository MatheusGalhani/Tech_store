# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='author',
            field=models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
