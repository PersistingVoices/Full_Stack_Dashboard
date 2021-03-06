# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csViewer', '0003_auto_20160914_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ps1',
            name='as_sold_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ps1',
            name='as_sold_margin_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ps1',
            name='as_sold_revenue',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ps1',
            name='ps1_margin_lgm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ps4',
            name='as_sold_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ps4',
            name='as_sold_margin_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ps4',
            name='as_sold_revenue',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ps4',
            name='ps4_margin_lgm',
            field=models.FloatField(),
        ),
    ]
