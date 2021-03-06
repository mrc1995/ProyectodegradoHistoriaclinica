# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-01 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0017_auto_20180301_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paraclinicos_aportados',
            fields=[
                ('Id_aportados', models.AutoField(max_length=35, primary_key=True, serialize=False, unique=True)),
                ('Para_aportados', models.CharField(max_length=800)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Historiaclinica.paciente')),
            ],
        ),
        migrations.RemoveField(
            model_name='medidas_antropometricas',
            name='Id_examen',
        ),
        migrations.DeleteModel(
            name='medidas_antropometricas',
        ),
    ]
