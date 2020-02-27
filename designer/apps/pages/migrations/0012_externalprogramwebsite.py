# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-25 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20190716_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalProgramWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.BooleanField(default=True, verbose_name='Display This Section')),
                ('header', models.CharField(default='Manage Your Degree', max_length=128, verbose_name='Header')),
                ('description', wagtail.core.fields.RichTextField(default="<p>Go to your program's portal to:</p><ul><li>Add or drop courses</li><li>Finance Department</li><li>Contact an advisor</li><li>Get your grade</li><li>Program wide discussions</li><li>and more</li></ul>", max_length=512, verbose_name='description')),
                ('link_display_text', models.CharField(max_length=128, verbose_name='Display Text')),
                ('link_url', models.URLField(verbose_name='URL')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_program_website', to='pages.ProgramPage', unique=True)),
            ],
        ),
    ]
