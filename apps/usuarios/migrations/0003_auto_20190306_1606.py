# Generated by Django 2.1.5 on 2019-03-06 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_categorias_clase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descargas',
            name='usu_pro',
        ),
        migrations.RemoveField(
            model_name='descargas',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Descargas',
        ),
    ]
