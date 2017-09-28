from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^openQpaperjson/', views.openQpaperjson,name='openQpaperjson'),
    url(r'^generate1Apaper/', views.generate1Apaper,name='generate1Apaper'),
    url(r'^generateqpaper/', views.generateqpaper,name='generateqpaper'),
    url(r'^generateqpaperbef/', views.generateqpaperbef,name='generateqpaperbef'),
    url(r'^questioncreate/', views.questioncreate,name='questioncreate'),
    url(r'^questionshow/', views.questionshow,name='questionshow'),
    url(r'^stulookpaper/', views.stulookpaper,name='stulookpaper'),
    url(r'^teachlookpaper/', views.teachlookpaper,name='teachlookpaper'),
    url(r'^teachlookapapersitu/', views.teachlookapapersitu,name='teachlookapapersitu'),
    url(r'^stulookresult/', views.stulookresult,name='stulookresult'),
    url(r'^teachpaperindex/', views.teachpaperindex,name='teachpaperindex'),
    url(r'^stupaperindex/', views.stupaperindex,name='stupaperindex'),
    url(r'^recieveanswer/', views.recieveanswer,name='recieveanswer'),
]
