#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:ldan 
@file: urls.py 
@time: 2018/04/{DAY} 
"""
from django.conf.urls import url
from django.contrib import admin

from ormsite.views import *


urlpatterns = [
    url(r'ormindex/$',ormindex,name='ormindex'),
    url(r'ommpindex/$',ommpindex,name='ommpindex'),
    url(r'orminfo/$',orminfo,name="orminfo"),
    url(r'orminfo/$',orminfo),
    url(r'ormlogout/$',ormlogout,name="ormlogout"),
    url(r'display_source_info',display_source_info,name="display_source_info"),
    url(r'display_target_info',display_target_info,name="display_target_info"),
    url(r'ormlogs/(?P<rid>\d+)/(?P<logtype>[0-1])/$',ormlogs,name='show_ormlogs'),
    url(r'check_process',check_process,name="check_process"),
    url(r'display_log',display_log,name="display_log"),
]