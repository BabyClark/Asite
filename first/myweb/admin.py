from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(MyDjangoUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['user','des','email','tools_sum']
    list_filter = ['user','tools_sum']
    search_fields = ['user','email']
    list_per_page = 20

@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ['id','tool_name','subject','size','time','belong_to']
    list_filter = ['tool_name','time','size','subject']
    search_fields = ['tool_name','subject','time','belong_to']
    list_per_page = 20

@admin.register(resources)
class resources(admin.ModelAdmin):
    list_display=['id','name','belong_to','time','size','subject']
    list_per_page = 20