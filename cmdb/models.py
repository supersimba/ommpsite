#coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



# IDC信息
class IDC(models.Model):
    idc_id = models.AutoField(primary_key=True)
    idcname = models.CharField(max_length=20,verbose_name=u'idc名')
    class Meta:
        db_table = 'idc'
        verbose_name = u'idc名'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.idcname


# IDC 机房信息
class ServerRoom(models.Model):
    roomname = models.CharField(max_length=20,verbose_name=u'服务器机房名')
    tag = models.CharField(max_length=20,verbose_name=u'机房标签名',unique=True)
    idc = models.ForeignKey(IDC,on_delete=models.CASCADE,verbose_name=u'所属IDC')

    class Meta:
        db_table = 'serverroom'
        verbose_name = u'机房名'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s(%s)' %(self.idc,self.tag)


# 机架信息
class Rack(models.Model):
    rackid = models.AutoField(primary_key=True)
    rack = models.IntegerField(verbose_name=u'机架号')
    serverroom = models.ForeignKey(ServerRoom,on_delete=models.CASCADE,verbose_name=u'所属机房')

    class Meta:
        db_table = 'rack'
        verbose_name=u'机架信息'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return '%s 机架号:%d' %(self.serverroom,self.rack)


# 机柜信息
class Cabinet(models.Model):
    cabid = models.AutoField(primary_key=True)
    cabinet = models.IntegerField(verbose_name=u'机柜号')
    rack = models.ForeignKey(Rack,on_delete=models.CASCADE,verbose_name=u'所属机架')


    class Meta:
        db_table = 'cabinet'
        verbose_name = u'机柜信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%d' %(self.cabinet)



# 资产类别分类表
class AssetCategory(models.Model):
    # asset_category_choices = (
    #     (1, '服务器'),
    #     (2, '网络设备'),
    #     (3, '安全设备'),
    #     (4, '存储设备'),
    #     (5, '机房设备'),
    #     (6, '软件资产')
    # )
    acid = models.AutoField(primary_key=True)
    catagory_name = models.CharField(max_length=30,unique=True,verbose_name=u'资产类别分类')

    class Meta:
        db_table='assetcategory'
        verbose_name = u'资产类别分类信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s' %(self.catagory_name)


# 资产类别表
class AssetClass(models.Model):
    acid = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50,unique=True,verbose_name=u'资产类别')
    assetcategory = models.ForeignKey(AssetCategory,verbose_name=u'资产类别分类')


    class Meta:
        db_table = 'assetclass'
        verbose_name = u'资产类别'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s>%s' %(self.assetcategory,self.class_name)

# 业务线
class BusinessLine(models.Model):
    name = models.CharField(verbose_name=u'业务线名', max_length=60, unique=True)
    memo = models.CharField(verbose_name=u'备注', max_length=200, blank=True)

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        db_table = 'businessline'
        verbose_name = u'业务线表'
        verbose_name_plural = verbose_name



# 资产表
class Asset(models.Model):
    assetid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,unique=True,verbose_name=u'资产名')
    asset_class = models.ForeignKey(AssetClass,verbose_name=u'资产类别')
    sn = models.CharField(max_length=128,unique=True,verbose_name=u'资产sn号')
    asset_ip = models.GenericIPAddressField(verbose_name=u'设备管理IP',blank=True,null=True)
    asset_admin = models.ForeignKey(User,verbose_name=u'资产负责人')
    asset_cabinet = models.ForeignKey(Cabinet,verbose_name=u'机柜号')
    asset_postion = models.IntegerField(verbose_name=u'机柜位',blank=True,null=True)
    trade_date = models.DateField(null=True,blank=True,verbose_name=u'购买日期')
    expire_date = models.DateField(null=True,blank=True,verbose_name=u'过保日期')
    price = models.FloatField(null=True,blank=True,verbose_name=u'购买价格(元)')
    asset_status_choices = (
        (0,'在线'),
        (1,'下线'),
        (2,'故障'),
        (3,'备用'),
        (4,'未知')
    )
    asset_status = models.IntegerField(choices=asset_status_choices,verbose_name=u'资产状态')
    create_date = models.DateTimeField(blank=True,auto_now_add=True,verbose_name=u'资产创建时间')
    update_date = models.DateTimeField(blank=True,auto_now=True,verbose_name=u'资产变更时间')
    businessline = models.ForeignKey(BusinessLine,verbose_name=u'所属业务线')


    class Meta:
        db_table='asset'
        verbose_name = u'资产信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s %s' %(self.name,self.asset_ip)


# 服务器表,和资产表1-v-1
class Server(models.Model):
    asset = models.OneToOneField(Asset,verbose_name=u'资产')
    model = models.CharField(verbose_name=u'产品型号',max_length=60,null=True,blank=True)
    os = models.CharField(verbose_name=u'操作系统',max_length=60,null=True,blank=True)

    class Meta:
        db_table ='server'
        verbose_name = u'服务器'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s sn:%s' %(Asset.name,Asset.sn)


