# Generated by Django 4.0.4 on 2022-06-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_cadeira_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='nome',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='topicos',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
    ]
