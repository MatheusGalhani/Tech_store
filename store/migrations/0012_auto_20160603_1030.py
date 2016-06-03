# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20160602_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='created_date',
            field=models.DateTimeField(verbose_name='Data de compra', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='carrinho',
            name='id_status',
            field=models.ForeignKey(verbose_name='Status', to='store.Statu'),
        ),
        migrations.AlterField(
            model_name='carrinho',
            name='usuario_compra',
            field=models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone_contato',
            field=models.CharField(verbose_name='Telefone', max_length=60),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao_produto',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem_produto',
            field=models.FileField(verbose_name='Imagem', upload_to=''),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(verbose_name='Nome', unique=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_produto',
            field=models.DecimalField(verbose_name='Preço de venda', decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qntd_produto',
            field=models.IntegerField(verbose_name='Quantidade de estoque', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor_compra',
            field=models.DecimalField(verbose_name='Preço de compra', decimal_places=2, max_digits=15),
        ),
    ]
