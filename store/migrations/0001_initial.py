# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=100)),
                ('descricao_produto', models.TextField()),
                ('preco_produto', models.DecimalField(max_digits=15, decimal_places=2)),
                ('qntd_produto', models.IntegerField()),
            ],
        ),
    ]
