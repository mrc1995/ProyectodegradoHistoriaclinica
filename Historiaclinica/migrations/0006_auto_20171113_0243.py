# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0005_paciente_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='Edad',
            field=models.CharField(max_length=12),
        ),
    ]