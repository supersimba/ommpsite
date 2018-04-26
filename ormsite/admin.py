#!usr/bin/env python
#-*- coding:utf-8 _*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin,User

from ormsite.models import UserProfile

from ormsite.models import *
# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True
    verbose_name_plural = 'UserProfile'


class UserProfileAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]

class QueueRelationUserInline(admin.TabularInline):
    model = QueueRelationUser
    extra = 1

class RepQueueAdmin(admin.ModelAdmin):
    filter_horizontal=('rqusers',)
    inlines = (QueueRelationUserInline,)
    search_fields = ['src_ip','tgt_ip']
    # list_editable=['describe','src_dbid',
    #                 'dbps_port','extract_port',
    #                 'tgt_dbid','collect_port']
    list_display = ['describe','src_ip','src_path','src_ssh_user','src_ssh_pwd','src_dbid',
                    'dbps_port','extract_port','tgt_ip','tgt_path','tgt_ssh_user','tgt_ssh_pwd',
                    'tgt_dbid','collect_port','src_script_path','tgt_script_path']

    fieldsets = (
        (
          None,{
              'fields':('describe',)
          }
        ),
        ('源端：',
         {
             'fields':('src_ip','src_path','src_ssh_user','src_ssh_pwd','src_dbid','dbps_port','extract_port','src_script_path')
         }
        ),
        ('目标端：',
         {
             'fields': ('tgt_ip','tgt_path','tgt_ssh_user','tgt_ssh_pwd','tgt_dbid','collect_port','tgt_script_path')
         }
        ),
    )

admin.site.unregister(User)
admin.site.register(User,UserProfileAdmin)

admin.site.register(rep_queue,RepQueueAdmin)