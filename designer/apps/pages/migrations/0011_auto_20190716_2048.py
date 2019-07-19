# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-16 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_programpage_idp_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.BooleanField(default=True, verbose_name='Display Program Documents')),
                ('header', models.CharField(default='Program Documents', max_length=128, verbose_name='Header for Program Documents')),
                ('documents', wagtail.wagtailcore.fields.StreamField((('file', wagtail.wagtailcore.blocks.StructBlock((('display_text', wagtail.wagtailcore.blocks.CharBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock())), icon='doc-full')), ('link', wagtail.wagtailcore.blocks.StructBlock((('display_text', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock())), icon='link'))), blank=True, verbose_name='Documents')),
            ],
        ),
        migrations.RemoveField(
            model_name='programpage',
            name='program_documents',
        ),
        migrations.AddField(
            model_name='programdocuments',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_documents', to='pages.ProgramPage', unique=True),
        ),
    ]