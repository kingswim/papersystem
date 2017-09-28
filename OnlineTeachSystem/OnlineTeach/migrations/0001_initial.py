# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_mark_chapter_difficult', models.TextField()),
                ('Question_id', models.CharField(max_length=30)),
                ('Question_description', models.TextField()),
                ('Question_point', models.IntegerField()),
                ('Question_type', models.CharField(max_length=24)),
                ('Question_default_answer', models.TextField()),
                ('Question_categery', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paper_id', models.CharField(max_length=30)),
                ('Paper_name', models.CharField(max_length=50)),
                ('Paper_key', models.CharField(max_length=50)),
                ('Paper_date', models.DateTimeField()),
                ('Paper_class', models.CharField(max_length=50)),
                ('Paper_marks', models.FloatField()),
                ('Paper_innerquestion_content', models.TextField()),
            ],
        ),
    ]
