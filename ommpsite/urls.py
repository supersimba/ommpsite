#coding:utf-8

from django.conf.urls import url,include
from django.contrib import admin

from ormsite.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^ommpsiteindex/$',ommpindex,name="ommpsiteindex"),
    #ormsite - url
    # url(r'^test',test),
    url(r'^ormsite/',include('ormsite.urls')),

    # url(r'^display_source_info/$',display_source_info,name="display_source_info"),

    # url(r'^check_process/$', check_process),
]
