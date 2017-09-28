# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
#today 把试卷组织起来,试卷在生成后就不跟question产生关系，作为独自存档的事物
#试卷可以用dict形式来存储
# Create your models here.

class Question(models.Model):
    Question_mark_chapter_difficult=models.TextField()
    Question_id=models.CharField(max_length=30)
    Question_description=models.TextField()
    Question_point=models.IntegerField()
    Question_type = models.CharField(max_length=24)
    Question_feature = models.CharField(max_length=50)
    Question_default_answer=models.TextField()
    Question_categery=models.CharField(max_length=30)
    Question_label=models.TextField(null=True,blank=True)

class QuestionPaper(models.Model):
    Paper_id=models.CharField(max_length=80)
    Paper_name=models.CharField(max_length=80)
    Paper_teacher_id=models.CharField(max_length=50,null=True)
    Paper_marks=models.FloatField(null=True)
    Paper_innerquestion_content=JSONField()

class AnswerPaper(models.Model):
    Ans_Paper_id=models.CharField(max_length=50)
    Ans_Paper_stu_id=models.CharField(max_length=30)
    Ans_QPaper_id = models.CharField(max_length=30,null=True)
    Ans_Paper_content=JSONField(null=True)
    Ans_Paper_puborpri=models.BooleanField()
    Ans_Paper_teachcomment=models.TextField(null=True)
    Ans_Paper_result=models.TextField(null=True)
    Ans_Paper_mark=models.CharField(max_length=30,null=True)
    Ans_Paper_startime=models.DateTimeField(null=True)
    Ans_Paper_endtime=models.DateTimeField(null=True)
    Ans_Paper_isclosed=models.BooleanField(default=False)


