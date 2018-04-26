#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:ldan 
@file: ormsetting.py 
@time: 2018/04/{DAY} 
"""
import os

# 站点根目录
SITE_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ormsite_parms = {
    'mysql_conn':{
        'host':'127.0.0.1',
        'port':'3306',
        'user':'root',
        'pwd':'simba2017',
        'dbname':'ommpdb'
    },
    'schd':{
        'frequency':2,
        'thrdnum':3
    }
}