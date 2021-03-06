# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0020_para_aportados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antecedentes',
            name='Familiares',
        ),
        migrations.RemoveField(
            model_name='antecedentes',
            name='Patologicos_medicamentos',
        ),
        migrations.RemoveField(
            model_name='antecedentes',
            name='Toxicos_alergicos',
        ),
        migrations.AddField(
            model_name='antecedentes',
            name='Alergicos',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='antecedentes',
            name='Farmacologicos',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='antecedentes',
            name='Patologicos',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='antecedentes',
            name='Toxicos',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='Habitos_riesgo',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='Habitos_saludables',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='Quirurgicos',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='Trau_emocionales',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='Trau_fisicos',
            field=models.CharField(max_length=800),
        ),
    ]
