# Generated by Django 2.0.6 on 2018-06-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='preco_compra',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Preço do Produto'),
        ),
    ]
