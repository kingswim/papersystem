# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect,render_to_response
from . import models
from . import myforms
from myforms import myforms
from models import Question,QuestionPaper,AnswerPaper
import random
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q,Avg
from django.template import Context
import itertools
import random

# Create your views here
@csrf_exempt
#学生从10章问卷中随机一张
def generateqpaper(request):
    if request.method=='GET':
            a1_difficult=request.GET['form_difficult']
            a1_mark=request.GET['form_mark']
            a1_chapter=request.GET['form_chapter']
            a1_teacher_name=request.GET['form_teacher_name']
            for i in range(0,10):
                record1=Question.objects.filter(Question_feature__icontains=a1_difficult).filter(Question_type='1').filter(Question_feature__icontains=a1_chapter).order_by('?').values()[:3]
                record2=Question.objects.filter(Question_feature__icontains=a1_difficult).filter(Question_type='2').filter(Question_feature__icontains=a1_chapter).order_by('?').values()[:1]
                record = itertools.chain(record1,record2)
                print record
                record_json=json.dumps(list(record),cls=DjangoJSONEncoder)
                print record_json
                QPaper_id=a1_difficult+a1_chapter+str(random.randint(i*40-i,i*40))
                QPaper_name =a1_difficult+a1_chapter+str(random.randint(i*40-i,i*40))
                QPaper_innerquestion_content=record_json
                QuestionPaper.objects.create(Paper_id=QPaper_id,
                                             Paper_name=QPaper_name,
                                             Paper_teacher_id=a1_teacher_name,
                                            Paper_innerquestion_content=QPaper_innerquestion_content
                )

            #t=Question.objects.filter(Question_type=)
            return HttpResponse("生成成功！")

#初步生成答卷表的学生id，问卷id，Apapeid，公测还是自测,其它为空,需要默认的学生的试题前缀
def generate1Apaper(request):
    if request.method=='GET':
        form=myforms.generate1Apaper()
        return render(request,'generate1Apaper.html',{'form':form})
    elif request.method=='POST':
        form=myforms.generate1Apaper(request.POST)
        if  form.is_valid():
           print form.cleaned_data['form_apaperstunums']
           apaperbef1 = form.cleaned_data['form_apaperbef']
           student_list_first= form.cleaned_data['form_apaperstunums']
           apaperstarttime= form.cleaned_data['form_Paper_startime']
           apaperendtime= form.cleaned_data['form_Paper_endtime']
           student_list_second=student_list_first.split('|')
           Qpaperidlist1=QuestionPaper.objects.filter(Paper_name__icontains=apaperbef1).values_list('Paper_name')
           print Qpaperidlist1
           Qpaperidlist =  [i[0] for  i in Qpaperidlist1 ]
           print Qpaperidlist

           for i in student_list_second:
               Qpaperid=random.choice(Qpaperidlist)
               AnsPaperid=str(i)+str(Qpaperid)
               AnswerPaper.objects.create(Ans_Paper_id=AnsPaperid,
                                          Ans_Paper_stu_id=i,
                                          Ans_QPaper_id=Qpaperid,
                                          Ans_Paper_puborpri=True,
                                          Ans_Paper_startime=apaperstarttime,
                                          Ans_Paper_endtime=apaperendtime,
                                          Ans_Paper_isclosed=True,

               )


    return HttpResponse("生成答卷表第一步ok")

#生成答卷表第二步 ：开放答卷接口，学生获取对应问卷，学生答卷，学生上传答案，自动生成客观题分数，进入老师批改状态
def openQpaperjson(request):
    if request.method=='GET':
                stuid=request.GET['form_stuid']
                record1=AnswerPaper.objects.filter(Ans_Paper_stu_id__icontains=stuid).filter(Ans_Paper_isclosed=True).values('Ans_QPaper_id')
                print record1
                record2=record1[0]['Ans_QPaper_id']
                print record2
                record=QuestionPaper.objects.filter(Paper_name=record2).values_list(u'Paper_innerquestion_content')[0]
                print record[0]
                print '*********************'
                a1=json.loads(record[0])
                print a1
                record = record[0].encode('utf-8')
                return HttpResponse(a1,content_type="application/json")
            
'''        
def generate2Apaper(request):
    if request.method=='GET':
        form=myforms.generate1Apaper()
        return render(request,'generate1Apaper.html',{'form':form})
    elif request.method=='POST':
        form=myforms.generate1Apaper(request.POST)
        if  form.is_valid():
           print form.cleaned_data['form_apaperstunums']
           apaperbef1 = form.cleaned_data['form_apaperbef']
           student_list_first= form.cleaned_data['form_apaperstunums']
           apaperstarttime= form.cleaned_data['form_Paper_startime']
           apaperendtime= form.cleaned_data['form_Paper_endtime']
           student_list_second=student_list_first.split('|')
           Qpaperidlist1=QuestionPaper.objects.filter(Paper_name__icontains=apaperbef1).values_list('Paper_name')
           print Qpaperidlist1
           Qpaperidlist =  [i[0] for  i in Qpaperidlist1 ]
           print Qpaperidlist

           for i in student_list_second:
               Qpaperid=random.choice(Qpaperidlist)
               AnsPaperid=str(i)+str(Qpaperid)
               AnswerPaper.objects.create(Ans_Paper_id=AnsPaperid,
                                          Ans_Paper_stu_id=i,
                                          Ans_QPaper_id=Qpaperid,
                                          Ans_Paper_puborpri=True,
                                          Ans_Paper_startime=apaperstarttime,
                                          Ans_Paper_endtime=apaperendtime,

               )


    return HttpResponse("生成答卷表第二步ok")
'''
#生成答卷表第三步:老师填写学生答卷最后分数与评价，统计本次考试结果
def generate3Apaper(request):
    if request.method=='GET':
        form=myforms.teachlookApaper()
        return render(request,'teachlookApaper.html',{'form':form})
    elif request.method=='POST':
        form=myforms.teachlookApaper(request.POST)
        if  form.is_valid():

               pass

    return HttpResponse("生成答卷表第一步ok")
@csrf_exempt
def generatequiz(request):
    if request.method=='GET':
            a1_difficult=request.GET['form_difficult']
            a1_mark=request.GET['form_mark']
            a1_chapter=request.GET['form_chapter']
            for i in range(0,10):
                record1=Question.objects.filter(Question_feature__icontains=a1_difficult).filter(Question_type='1').filter(Question_feature__icontains=a1_chapter).order_by('?').values()[:3]
                record2=Question.objects.filter(Question_feature__icontains=a1_difficult).filter(Question_type='2').filter(Question_feature__icontains=a1_chapter).order_by('?').values()[:1]
                record = itertools.chain(record1,record2)
                print record
                record_json=json.dumps(list(record),cls=DjangoJSONEncoder)
                print record_json

                #t=Question.objects.filter(Question_type=)
            return HttpResponse(record_json,content_type="application/json")


def questioncreate(request):
    if request.method=='GET':
        form=myforms.questioncreate()
        return render(request,'questioncreate.html',{'form':form})
    elif request.method=='POST':
        form=myforms.questioncreate(request.POST)
        if  form.is_valid():
           print form.cleaned_data['form_Question_feature']
           Question.objects.create(
               Question_id= form.cleaned_data['form_Question_id'],
               Question_description=form.cleaned_data['form_Question_description'],
               Question_point=form.cleaned_data['form_Question_point'],
               Question_type=form.cleaned_data['form_Question_type'],
               Question_label=form.cleaned_data['form_Question_label'],
               Question_feature=form.cleaned_data['form_Question_feature'],
               Question_default_answer=form.cleaned_data['form_Question_default_answer'],
               Question_categery=form.cleaned_data['form_Question_categery'],


           )
           return HttpResponse('插入成功！')

def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render_to_response("index.html")

def questionshow(request):
    return render_to_response("questionshow.html")
@csrf_exempt
def getpaper(request):
    return render_to_response("getpaper.html")

def stulookpaper(request):
    if request.method=='GET':
        form=myforms.stulookpaper()
        return render(request,'stulookpaper.html',{'form':form})
    elif request.method=='POST':
        form=myforms.stulookpaper(request.POST)
        if  form.is_valid():
            stuid=form.cleaned_data['form_stuid']
            return render(request,'foo.html',{'stuid':stuid})

def teachlookpaper(request):
    if request.method=='GET':
        form1=myforms.teachlookpaper()
        form2=myforms.teachlookpaper2()
        return render(request,'teachlookApaper.html',{'form1':form1,'form2':form2})
    elif request.method=='POST':
        form1=myforms.teachlookpaper(request.POST)
        form2=myforms.teachlookpaper2(request.POST)
        try:
            print form1
        except KeyError:
            flag1=False
        try:
            print form2
        except KeyError:
            flag2=False

        if  form1.is_valid() and flag2==False :
            stuid=form1.cleaned_data['form_stuid']
            sametermpaperid = form1.cleaned_data['form_sametermpaperid']
            result = AnswerPaper.objects.filter(Ans_QPaper_id__icontains=sametermpaperid).filter(Ans_Paper_stu_id=stuid).filter(Ans_Paper_isclosed=1).values('Ans_Paper_mark','Ans_Paper_result','Ans_Paper_content','Ans_QPaper_id')
            Qpaper_id=result[0]['Ans_QPaper_id']
            result1 = QuestionPaper.objects.filter(Paper_name=Qpaper_id).values('Paper_innerquestion_content')
            print result1
            result1 =result1[0]['Paper_innerquestion_content']
            t2=json.loads(result1)
            print '**************************'
            print t2
            print '**************************'
            t2=json.loads(t2)
            lista4=[i['Question_point'] for i in t2] 
            t2=[i['Question_default_answer'] for i in t2]
            print t2
            print result[0]
            middlemark= result[0]['Ans_Paper_mark']
            middleresult= result[0]['Ans_Paper_result']
            t=result[0]['Ans_Paper_content']
            t1=json.loads(t.decode('string-escape').strip('"'))
            #t1=json.loads(t1.decode('string-escape').strip('"'))
            print t1
            #问题本身，问题答案，问题默认答案,问题分值
            questiontuple=()
            questionlist=t1['question']
            print '********************************'
            print questionlist
            print '********************************'
            lista1=[i['question'] for i in  questionlist]
            lista2=[i['answer'] for i in  questionlist]
            lista3=t2
            lista=[(lista1[i],lista2[i],lista3[i],lista4[i]) for i in range(0,len(lista1))]
             
            return render(request,'teachlookApaper.html',{'list2':lista,'form2':form2,'stuid':stuid,'Qpaperid':Qpaper_id,'middlemark':middlemark,'middleresult':middleresult})

        elif form2.is_valid() and flag1==False:
            form_compaperid=form2.cleaned_data['form_compaperid']
            form_comstuid=form2.cleaned_data['form_comstuid']
            form_endpoint=form2.cleaned_data['form_endpoint']
            form_comment=form2.cleaned_data['form_comment']
            form_resultradio=form2.cleaned_data['form_resultradio']
            tempres=AnswerPaper.objects.filter(Ans_QPaper_id=form_compaperid).filter(Ans_Paper_stu_id=form_comstuid)
            if tempres==[]:
                return HttpResponse('看看有没有输错！')
            else:
                print '?????????????????????????'
                tempres.update(Ans_Paper_teachcomment=form_comment,
                               Ans_Paper_mark=form_endpoint,
                               Ans_Paper_isclosed=False,


                )

            return HttpResponse('修改成功！')
     

def stulookresult(request):
    if request.method=='GET':
        form1=myforms.stulookpaper()
        return render(request,'stulookresult.html',{'form1':form1})
    elif request.method=='POST':
        form1=myforms.stulookpaper(request.POST)
        if form1.is_valid():
            stuid=form1.cleaned_data['form_stuid']
            sametermpaperid = form1.cleaned_data['form_sametermpaperid']
            result = AnswerPaper.objects.filter(Ans_QPaper_id__icontains=sametermpaperid).filter(Ans_Paper_stu_id=stuid).values('Ans_Paper_mark','Ans_Paper_result','Ans_Paper_content','Ans_QPaper_id','Ans_Paper_teachcomment')
            print result
            d={}
            index=0
            print result[0]
            print result[1]
            print len(result)
            for i in range(0,len(result)):
                print i
                t=''
                t+=str(result[i]['Ans_QPaper_id'])+'|'
                t+=str(result[i]['Ans_Paper_mark'])+'|'
                t+=str(result[i]['Ans_Paper_result'])+'|'
                t+=str(result[i]['Ans_Paper_teachcomment'])+'|'
                d[i]=t
                
            print d 
            return render(request,'stulookresult.html',{'d':d})

def testvue(request):
    return render_to_response("foo.html")

@csrf_exempt
def recieveanswer(request):
    if request.method == 'POST':
        received_json_data =json.loads(request.body)
        print received_json_data
        print type(received_json_data)
        record_json=json.dumps(received_json_data,cls=DjangoJSONEncoder)
        print record_json
        record_json1=json.dumps(record_json,cls=DjangoJSONEncoder)
        print record_json1
        stuid = received_json_data['stuid']
        Qpaperid=AnswerPaper.objects.filter(Ans_Paper_stu_id=stuid).values('Ans_QPaper_id' )[0]['Ans_QPaper_id']
        print Qpaperid
        record=QuestionPaper.objects.filter(Paper_name=Qpaperid).values_list(u'Paper_innerquestion_content')[0]
        print record[0]
        a1=json.loads(record[0])
        print a1
        print type(a1)
        a2=json.loads(a1)
        print a2
        print type(a2)
        radiosum=0
        sum=0
        count_correct=0
        count_uncorrect=0
        for i in range(0,4):
            print a2[i]["Question_default_answer"]
            print a2[i]["Question_point"]
            print received_json_data["question"][i]['answer']
            if a2[i]["Question_default_answer"]==received_json_data["question"][i]['answer']:
                radiosum+=int(a2[i]["Question_point"])
                sum+=int(a2[i]["Question_point"])
                count_correct+=1
            else:
                radiosum+=0
                sum+=int(a2[i]["Question_point"])
                count_uncorrect+=1

        resultradiosum=str(radiosum)
        resultradio=str(count_correct)+'|'+str(count_uncorrect)
        AnswerPaper.objects.filter(Ans_Paper_stu_id=stuid).filter(Ans_Paper_isclosed=1).update(
            Ans_Paper_mark=resultradiosum,
            Ans_Paper_result=resultradio,
            Ans_Paper_content=record_json, 
            
        )
        return HttpResponse('回收成功!')

def teachpaperindex(request):
        return render(request,'teachpaperindex.html')

def stupaperindex(request):
        return render(request,'stupaperindex.html')

def generateqpaperbef(request):
    if request.method == 'GET':
        form=myforms.generatepaperbef() 
        return render(request,'generatepaper.html',{'form':form})

def teachlookapapersitu(request):
    if request.method == 'GET':
        form=myforms.teachlookpapersitu()
        return render(request,'teachlookpapersitu.html',{'form':form})
    elif request.method=='POST':
        form1=myforms.teachlookpapersitu(request.POST)
        if form1.is_valid():
            sametermpaperid=form1.cleaned_data['form_sametermpaperid']
            pointrange=form1.cleaned_data['form_pointrange']
            AVGmark=AnswerPaper.objects.filter(~Q(Ans_Paper_mark='')).filter(Ans_QPaper_id__icontains=sametermpaperid).aggregate(Avg('Ans_Paper_mark'))['Ans_Paper_mark__avg']
        return render(request,'teachlookpapersitu.html',{'AVG':AVGmark})
