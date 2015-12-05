# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maproulette', '0002_auto_20151204_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='slug',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='maproulette.Challenge'),
        ),
        migrations.AlterField(
            model_name='task',
            name='identifier',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
