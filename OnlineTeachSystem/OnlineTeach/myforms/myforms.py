# -*- coding: utf-8 -*- 
from django.forms import Form
from django.forms import widgets
from django.forms import fields
from django.core.validators import RegexValidator
import re
from .. import models

class generatequiz(Form):
    form_difficult=fields.CharField(max_length=30)
    form_mark=fields.CharField(max_length=30)
    form_chapter=fields.CharField(max_length=30)
    def clean(self):
            cleaned_data= super(generatequiz,self).clean()
            form_difficult=cleaned_data['form_difficult']
            form_mark=cleaned_data['form_mark']
            form_chapter=cleaned_data['form_chapter']
            return cleaned_data


class generate1Apaper(Form):
    form_apaperstunums=fields.CharField(widget=widgets.Textarea)
    form_apaperbef=fields.CharField(max_length=30)
    form_Paper_startime=fields.DateTimeField(required=True,input_formats=['%Y-%m-%d-%H-%M'],error_messages={'required':'时间不能为空'})
    form_Paper_endtime=fields.DateTimeField(required=True,input_formats=['%Y-%m-%d-%H-%M'],error_messages={'required':'时间不能为空'})
    def clean(self):
            cleaned_data= super(generate1Apaper,self).clean()
            form_apaperstunums=cleaned_data['form_apaperstunums']
            form_apaperbef=cleaned_data['form_apaperbef']
            form_Paper_startime=cleaned_data['form_Paper_startime']
            form_Paper_endtime=cleaned_data['form_Paper_endtime']
            return cleaned_data

class stulookpaper(Form):
    form_stuid=fields.CharField(max_length=30)
    def clean(self):
        cleaned_data= super(stulookpaper,self).clean()
        form_stuid=cleaned_data['form_stuid']
        return cleaned_data

class teachlookpapersitu(Form):
    form_sametermpaperid=fields.CharField(max_length=30)
    form_pointrange=fields.CharField(max_length=30)
    def clean(self):
        cleaned_data= super(teachlookpapersitu,self).clean()
        form_sametermpaperid=cleaned_data['form_sametermpaperid']
        form_pointrange=cleaned_data['form_pointrange']
        return cleaned_data
    
class teachlookpaper(Form):
    form_sametermpaperid=fields.CharField(max_length=30)
    form_stuid=fields.CharField(max_length=30)
    def clean(self):
        cleaned_data= super(teachlookpaper,self).clean()
        form_sametermpaperid=cleaned_data['form_sametermpaperid']
        form_stuid=cleaned_data['form_stuid']
        return cleaned_data
    

class teachlookpaper2(Form):
    form_compaperid=fields.CharField(max_length=30)
    form_comstuid=fields.CharField(max_length=30)
    form_endpoint=fields.CharField(max_length=30)
    form_comment=fields.CharField(max_length=30,widget=widgets.Textarea)
    form_resultradio=fields.CharField(max_length=30)
    def clean(self):
        cleaned_data= super(teachlookpaper2,self).clean()
        form_compaperid=cleaned_data['form_compaperid']
        form_comstuid=cleaned_data['form_comstuid']
        form_endpoint=cleaned_data['form_endpoint']
        form_comment=cleaned_data['form_comment']
        form_resultradio=cleaned_data['form_resultradio']
        return cleaned_data
    
class teachlookApaper2(Form):
    form_compaperid=fields.CharField(max_length=30)
    form_comstuid=fields.CharField(max_length=30)
    form_comment=fields.CharField(max_length=30)
    form_endpoint=fields.CharField(max_length=30)
    form_resultradio=fields.CharField(max_length=30)
    def clean(self):
        cleaned_data= super(teachlookApaper2,self).clean()
        form_compaperid=cleaned_data['form_compaperid']
        form_comstuid=cleaned_data['form_comstuid']
        form_comment=cleaned_data['form_comment']
        form_endpoint=cleaned_data['form_endpoint']
        form_resultradio=cleaned_data['form_resultradio']
        return cleaned_data

class generatepaperbef(Form):
    form_difficult=fields.CharField(max_length=30)
    form_mark=fields.CharField(max_length=30)
    form_chapter=fields.CharField(max_length=30)
    form_teacher_name=fields.CharField(max_length=30)
    def clean(self):
        cleaned_data= super(generatepaperbef,self).clean()
        form_difficult=cleaned_data['form_difficult']
        form_mark=cleaned_data['form_mark']
        form_chapter=cleaned_data['form_chapter']
        form_teacher_name=cleaned_data['form_teacher_name']
        return cleaned_data

class questioncreate(Form):
    form_Question_id = fields.CharField(max_length=30)
    form_Question_description = fields.CharField(widget=widgets.Textarea)
    form_Question_point = fields.IntegerField()
    form_Question_type = fields.CharField(max_length=24)
    form_Question_label = fields.CharField(widget=widgets.Textarea)
    form_Question_feature = fields.CharField(max_length=50)
    form_Question_default_answer = fields.CharField(widget=widgets.Textarea)
    form_Question_categery = fields.CharField(max_length=30)
    def clean(self):
            cleaned_data= super(questioncreate,self).clean()
            form_Question_id=cleaned_data.get('form_Question_id')
            form_Question_description=cleaned_data.get('form_Question_description')
            form_Question_point=cleaned_data.get('form_Question_point')
            form_Question_type=cleaned_data.get('form_Question_type')
            form_Question_label=cleaned_data.get('form_Question_label')
            form_Question_feature=cleaned_data.get('form_Question_feature')
            form_Question_default_answer=cleaned_data.get('form_Question_default_answer')
            form_Question_categery=cleaned_data.get('form_Question_categery')
            if form_Question_id and form_Question_description and form_Question_feature and form_Question_point and form_Question_type and form_Question_label and  form_Question_default_answer and form_Question_categery :
                    return cleaned_data
