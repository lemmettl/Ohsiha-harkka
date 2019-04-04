# Generated by Django 2.1.5 on 2019-03-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koirapuisto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=30)),
                ('viheralueen_osan_id', models.CharField(max_length=30)),
                ('alueen_nimi', models.CharField(max_length=30)),
                ('alueen_sijainti', models.CharField(max_length=30)),
                ('alueen_osan_sijainti', models.CharField(max_length=30)),
                ('pinta_ala', models.IntegerField(max_length=30)),
                ('kayttoluokka', models.CharField(max_length=10)),
                ('hoitoluokka', models.CharField(max_length=10)),
                ('urakka_alue', models.CharField(max_length=10)),
                ('kaupunginosa', models.CharField(max_length=10)),
                ('tilaaja', models.CharField(max_length=10)),
                ('kunnossapitaja', models.CharField(max_length=10)),
                ('erityiskaytto', models.CharField(max_length=10)),
                ('kunnossapitokausi', models.CharField(max_length=10)),
                ('toimiluokka', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]