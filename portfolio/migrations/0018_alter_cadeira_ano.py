# Generated by Django 4.0.4 on 2022-06-17 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_alter_cadeira_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ano',
            field=models.IntegerField(default=1),
        ),
    ]
