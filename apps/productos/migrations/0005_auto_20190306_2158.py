# Generated by Django 2.1.5 on 2019-03-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20190306_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
