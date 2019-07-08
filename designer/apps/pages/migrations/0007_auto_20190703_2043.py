# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-03 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20190702_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpagebranding',
            name='site_title',
            field=models.CharField(max_length=128, null=True, verbose_name='Site Title'),
        ),
        migrations.AlterField(
            model_name='programpagebranding',
            name='program_title',
            field=models.CharField(max_length=128, null=True, verbose_name='Program Title'),
        ),
    ]
