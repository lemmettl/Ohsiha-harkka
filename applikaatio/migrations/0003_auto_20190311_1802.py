# Generated by Django 2.1.5 on 2019-03-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0002_auto_20190311_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koirapuisto',
            name='pinta_ala',
            field=models.IntegerField(),
        ),
    ]