# Generated by Django 5.0.6 on 2024-06-24 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domoticapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donnee',
            name='id_capteur',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='domoticapp.capteur'),
        ),
    ]
