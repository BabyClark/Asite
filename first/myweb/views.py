from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .userform import MyUser,UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login as log

from .models import MyDjangoUser,Tools
from django.core.paginator import Paginator
# Create your views here.

def hellow(req):
    return HttpResponse("hellow")
def index(req):
    limit=6
    simple=Tools.objects.all()
    page_data=Paginator(simple,limit)
    page_way=req.GET.get('page',1)
    load=page_data.page(page_way)
    con={
        'obs':load,
        'count':simple.count()
    }
    return render(req,'index.html',con)

#用户注册界面
def createUser(request):
    if request.method=='POST':
        #user=MyUser(request.POST)
        user=UserCreationForm(request.POST)
        if user.is_valid():
            new_user=User.objects.create_user(
                username=user.cleaned_data["username"],
                password=user.cleaned_data["password1"],
            )
            login_user = authenticate(username=user.cleaned_data["username"], password=user.cleaned_data["password1"])
            log(request, login_user)
            return HttpResponseRedirect('/')
        else:
            con={
                'user':user,
                 "error": ''
                 }
            return render(request,'login.html',context=con)
    else:
        con = {
            "error": ''
        }
        return render(request,'/error/',con)

#用户登录界面
from .userform import Login
def login(request):
    if request.method=='POST':
        user=Login(request.POST)
        if user.is_valid():
            username=user.cleaned_data['username']
            password=user.cleaned_data['password']
            # username=request.POST.get("username")
            # password=request.POST.get("password")
            user = authenticate(username=username, password=password)
        if user is not None:
            log(request,user)
            return HttpResponseRedirect('/site/')
        else:
            error="用户名或密码错误"
            con={
                "error":error
            }
            return render(request,'login.html',context=con)
    else:
        user=Login()
        con={
            'user':user,
            'error':""
        }
        return render(request,'login.html',context=con)

#index界面
from django.contrib.auth.decorators import login_required
# @login_required(login_url='/login/')
def mainindex(request):
    user=User(request.user)
    return render(request,'mainindex.html')


def toolsindex(request,tid):
    this_tool=Tools.objects.get(id=tid)
    con={
        'tool':this_tool
    }
    return render(request,'toolsindex.html',context=con)
#下载
from django.http import FileResponse,StreamingHttpResponse
from django.conf import settings
import os
import mimetypes
def download(request,tid):
    this_tool = Tools.objects.get(id=tid)
    name=str(this_tool.id)+'.zip'
    path_name='code/'+name
    filepath = os.path.join(settings.MEDIA_ROOT, path_name)
    con_type = mimetypes.guess_type(filepath)[0]
    response=StreamingHttpResponse(open(filepath,'rb'),content_type=con_type)
    response['Content-Disposition'] = 'filename=' + name
    # print(this_tool.tool_name)
    return response

def user(request,error=None):
    userpro=MyDjangoUser.objects.get(user=request.user)
    con={
        'userpro':userpro,
        'error':error
    }
    return render(request,'user.html',con)

from .userform import user_message
def user_change(request):
    user_pro=user_message(request.POST)
    if user_pro.is_valid():
        userchang=User.objects.get(username=request.user)
        userchang.username=user_pro.cleaned_data['username']
        if User.objects.filter(username=user_pro.cleaned_data['username']).exists() and userchang.username!=request.user.username :
            error = '该用户名已存在'
            return user(request,error)
        else:
            userprochange=MyDjangoUser.objects.get(user=request.user)
            userprochange.user.username=user_pro.cleaned_data['username']
            userprochange.email=user_pro.cleaned_data['email']
            userprochange.school = user_pro.cleaned_data['school']
            userprochange.subject = user_pro.cleaned_data['subject']
            userprochange.des = user_pro.cleaned_data['des']
            userchang.save()
            userprochange.save()
            return HttpResponseRedirect('/site/user/')
    else:return HttpResponseRedirect('/site/user/')

# def up_head_portrait(request):
#     return HttpResponse('sucess')
#
# def modify(request):
#     return render(request,'new_user2.html')

#联系站长
from .userform import  user_email
from .sendemail import sendemail
def contact(request):
    status=False
    if request.method=='GET':
        con={
            'status':status
        }
        return render(request,'contact.html',con)
    else:
        email=user_email(request.POST)
        if email.is_valid():
            adress=email.cleaned_data['email']
            content=email.cleaned_data['content']
            name=request.user.username
            sendemail(name,adress,content)
            status=True
            con = {
                'status': status
            }
            return render(request,'contact.html',con)
        con={
            'status': status,
            'error':'您输入的信息有误，请重新输入'
        }
        return render(request,'contact.html',con)
from .userform import message
def indexmessage(request):
    email = message(request.POST)
    if email.is_valid():
        adress = email.cleaned_data['email']
        messages = email.cleaned_data['messages']
        phone=email.cleaned_data['phone']
        name=email.cleaned_data['name']
        content=str(str(phone)+'-->'+str(message))
        #content='jsjsjsja'
        sendemail(name,adress,messages)
        return HttpResponseRedirect('/site/')


#上传文件
from django.conf import settings
import codecs
# coding=utf8
#-*-coding:utf-8-*-
# def upfiles(request):
#     if request.method == "POST":
#         f=request.FILES["file"]
#         filePath=os.path.join(settings.MEDIA_ROOT,f.name)
#         with codecs.open(filePath.encode('utf8'),'a',encoding='utf8') as fp:
#             for info in f.chunks():
#                 fp.write(str(info))
#         #Oldfile=filePath
#         #Newfile=os.path.join(settings.MEDIA_ROOT,'{}.jpg'.format(request.user))
#         #os.replace(Oldfile,Newfile)
#         return HttpResponse("success")
#     else:
#         return render(request,'upload.html')

from .userform import uploadfile
from .models import resources
def upfiles(request):
    if request.method == 'POST':
        file=uploadfile(request.POST,request.FILES)
        if file.is_valid():
            f = request.FILES["file"]
            if f.size>52428800:
                return HttpResponse('bigger')
            filePath = os.path.join(settings.MEDIA_ROOT, f.name)
            with codecs.open(filePath.encode('utf8'), 'a', encoding='utf8') as fp:
                for info in f.chunks():
                    fp.write(str(info))
            belongto=MyDjangoUser.objects.get(user=request.user)
            fileobj=resources(
                name=file.cleaned_data['name'],
                subject=file.cleaned_data['subject'],
                belong_to=belongto
            )

            fileobj.save()
            return HttpResponse('sucess')
    else:
        return render(request,'upload.html')



def m78(request):
    return render(request,'m78.html')

def page_not_found(req):
    return render(req,'404.html')

def server_error(req):
    return render(req,'500.html')

