# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-11-14 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201111_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='category',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
