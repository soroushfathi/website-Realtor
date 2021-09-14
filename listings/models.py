from django.db import models
from django.db.models.fields import FloatField
from realtors.models import Realtor
from datetime import datetime

TYPES = (('ویلا','ویلا'),('آپارتمان','آپارتمان'),('تجاری','تجاری'),('فروشگاه','فروشگاه'),)
CONDITION = (('اجاره' ,'اجاره'), ('فروش' ,'فروش'),)
PROVINCES = (('گلستان','گلستان'),('خراسان رضوی','خراسان رضوی'),('مازندران','مازندران'),)
GOLESTAN_CITIES = (('گرگان','گرگان'),('کردکوی','کردکوی'),('بندرگز','بندرگز'),('گنبد','گنبد'),)

class Listings(models.Model):
    realtor  = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    title    = models.CharField(max_length=100, blank=False)
    types = models.CharField(choices=TYPES,max_length=128,default='آپارتمان')
    city = models.CharField(choices=GOLESTAN_CITIES,max_length=128,default='آپارتمان')
    address  = models.TextField()
    bedroom  = models.IntegerField(default=1)
    bathroom = models.IntegerField(default=1)
    inrastructure = models.FloatField(default=0.0)
    detail   = models.TextField()
    is_published = models.BooleanField(default=True)
    is_sold  = models.BooleanField(default=False)
    list_data = models.DateTimeField(blank=True,default=datetime.now)
    memorandum = models.FileField()
    floor = models.IntegerField(null=True) #  null=True -> default
    condition = models.CharField(choices=CONDITION,max_length=128, default='اجاره')
    price= FloatField(default=0.0)
    main_photo = models.ImageField(blank=True)
    # main_photo = models.ImageField(uplaod_to='photos/% Y/% m/% d/', blank=True)
    photo1 = models.ImageField(blank=True)
    photo2 = models.ImageField(blank=True)

    def __str__(self):
        return 'title: ' + self.title

