# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-22 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20190622_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
