# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csViewer', '0014_auto_20161103_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterfall',
            name='cosElementName',
            field=models.CharField(default='cosElementName', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='waterfall',
            name='curr',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='waterfall',
            name='fin',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='waterfall',
            name='nDiff',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='waterfall',
            name='pDiff',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='waterfall',
            name='start',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
    ]
