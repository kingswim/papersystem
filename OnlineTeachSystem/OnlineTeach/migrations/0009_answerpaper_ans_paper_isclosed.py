# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTeach', '0008_auto_20170731_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerpaper',
            name='Ans_Paper_isclosed',
            field=models.BooleanField(default=False),
        ),
    ]
