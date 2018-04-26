#!usr/bin/env python
#-*- coding:utf-8 _*-

from django.contrib import admin

from cmdb.models import *
# Register your models here.

class IDCAdmin(admin.ModelAdmin):
    list_display = ['idc_id','idcname']


class ServerRoomAdmin(admin.ModelAdmin):
    list_display = ['roomname','tag','idc']


# class CabinetInline(admin.StackedInline):
#     model = Cabinet


class RackAdmin(admin.ModelAdmin):
    list_display = ['serverroom','rack']
    # inlines = [CabinetInline]


class CabinetAdmin(admin.ModelAdmin):
    list_display = ['rack','cabinet']


class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ['acid','catagory_name']


class AssetClassAdmin(admin.ModelAdmin):
    list_display = ['class_name','assetcategory']


class BusinessLineAdmin(admin.ModelAdmin):
    list_display = ['name','memo']


class AssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'asset_class', 'sn', 'asset_ip', 'asset_admin', 'asset_cabinet',
                    'asset_postion', 'trade_date', 'expire_date', 'price', 'asset_status', 'create_date', 'update_date',
                    'businessline']



admin.site.register(IDC,IDCAdmin)
admin.site.register(ServerRoom,ServerRoomAdmin)
admin.site.register(Rack,RackAdmin)
admin.site.register(Cabinet,CabinetAdmin)

admin.site.register(AssetCategory,AssetCategoryAdmin)
admin.site.register(AssetClass,AssetClassAdmin)
admin.site.register(Asset,AssetAdmin)
admin.site.register(BusinessLine,BusinessLineAdmin)