# Generated by Django 4.0.4 on 2022-06-05 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_cadeira_imagem_alter_professor_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
