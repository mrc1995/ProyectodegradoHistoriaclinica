# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0011_paraclinicos_id_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen_fisico',
            name='Estatura',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='examen_fisico',
            name='FC',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='examen_fisico',
            name='FR',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='examen_fisico',
            name='IMC',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='examen_fisico',
            name='Perimetro_cintura',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='examen_fisico',
            name='Peso',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='examen_fisico',
            name='Pulso',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='examen_fisico',
            name='TA',
            field=models.CharField(max_length=50),
        ),
    ]
