# Generated by Django 2.1.5 on 2019-03-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0004_auto_20190313_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arvostelu',
            old_name='kommentit',
            new_name='kommentti',
        ),
        migrations.AddField(
            model_name='arvostelu',
            name='otsikko',
            field=models.CharField(default='ei otsikkoa', max_length=15),
        ),
    ]