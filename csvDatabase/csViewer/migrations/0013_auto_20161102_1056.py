# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-02 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csViewer', '0012_waterfall'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waterfall',
            old_name='end',
            new_name='fin',
        ),
        migrations.RenameField(
            model_name='waterfall',
            old_name='ndiff',
            new_name='nDiff',
        ),
        migrations.RenameField(
            model_name='waterfall',
            old_name='pdiff',
            new_name='pDiff',
        ),
        migrations.AddField(
            model_name='waterfall',
            name='curr',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
    ]
