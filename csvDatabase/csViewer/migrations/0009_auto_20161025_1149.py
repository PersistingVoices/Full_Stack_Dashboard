# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csViewer', '0008_auto_20161025_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db1',
            name='cusNo',
            field=models.CharField(max_length=255),
        ),
    ]
