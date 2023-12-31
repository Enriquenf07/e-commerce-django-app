# Generated by Django 4.2.1 on 2023-05-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_produto_descricao_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
    ]
