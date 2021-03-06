# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTeach', '0003_auto_20170724_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ans_Paper_id', models.CharField(max_length=50)),
                ('Ans_Paper_stu_id', models.CharField(max_length=30)),
                ('Ans_QPaper_id', models.CharField(max_length=30, null=True)),
                ('Ans_Paper_content', jsonfield.fields.JSONField(null=True)),
                ('Ans_Paper_puborpri', models.BooleanField()),
                ('Ans_Paper_teachcomment', models.TextField(null=True)),
                ('Ans_Paper_result', models.TextField(null=True)),
                ('Ans_Paper_mark', models.CharField(max_length=30, null=True)),
                ('Ans_Paper_startime', models.DateTimeField(null=True)),
                ('Ans_Paper_endtime', models.DateTimeField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='questionpaper',
            old_name='Paper_class',
            new_name='Paper_range',
        ),
        migrations.RemoveField(
            model_name='questionpaper',
            name='Paper_date',
        ),
        migrations.RemoveField(
            model_name='questionpaper',
            name='Paper_key',
        ),
    ]
