# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_finacial_data', '0004_auto_20161128_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='asset',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fetch_finacial_data.Asset'),
            preserve_default=False,
        ),
    ]
