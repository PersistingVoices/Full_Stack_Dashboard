# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csViewer', '0010_db1_coselementnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='db1',
            name='ps1',
            field=models.FloatField(default=float),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='db1',
            name='ps3',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
    ]
