# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maproulette', '0003_auto_20151205_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maproulette.Challenge'),
        ),
    ]
