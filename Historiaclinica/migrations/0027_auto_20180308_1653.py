# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0026_recomendaciones_solicitud_ayudas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostico',
            name='Nombre',
        ),
        migrations.RemoveField(
            model_name='diagnostico',
            name='codigo',
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='Codigo_Nombre',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
