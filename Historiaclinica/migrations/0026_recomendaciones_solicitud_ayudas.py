# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0025_auto_20180308_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendaciones',
            fields=[
                ('Id_recomendacion', models.AutoField(max_length=35, primary_key=True, serialize=False, unique=True)),
                ('Recomendacion', models.CharField(max_length=800)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Historiaclinica.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud_ayudas',
            fields=[
                ('Id_solicitud', models.AutoField(max_length=35, primary_key=True, serialize=False, unique=True)),
                ('Solicitud_ayudas_diag', models.CharField(max_length=800)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Historiaclinica.paciente')),
            ],
        ),
    ]
