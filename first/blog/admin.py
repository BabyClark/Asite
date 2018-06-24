from django.contrib import admin
from   .models import *
# Register your models here.

@admin.register(artical)
class articalAdmin(admin.ModelAdmin):
    list_display=['id','title','writer','time','viewtimes','commment_times','abstract','subject']
    list_filter = ['id','subject','time','writer']
    class Media:
        js=(
            'js/kindeditor/kindeditor-all.js',
            'js/kindeditor/lang/zh-CN.js',
            'js/kindeditor/config.js'
        )

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display=['name','time','text','belong_to']

@admin.register(MyBlogUser)
class MyBlogUserAdmin(admin.ModelAdmin):
    list_display=['user','email','des']

@admin.register(artical_count)
class ArticalCountAdmin(admin.ModelAdmin):
    list_display=['id','movienum','lifenum','studynum','djangojznum']