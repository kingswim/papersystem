# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTeach', '0004_auto_20170727_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Question_label',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='Paper_innerquestion_content',
            field=jsonfield.fields.JSONField(),
        ),
    ]
