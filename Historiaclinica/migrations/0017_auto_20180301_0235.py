# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-01 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0016_auto_20180228_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='Fecha_atencion',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='Hora_atencion',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='Nivel_educativo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
