from django.conf.urls import url
from . import views
#import first
import os
import django
app_name = 'myweb'
from django.contrib.auth.views import logout_then_login

urlpatterns=[
    url(r'^index$',views.index,name="home"),
    url(r'^m78/$',views.m78,name='m78'),
    # url(r'^hellow/$',views.hellow,name='hellow'),
    url(r'^signup/$',views.createUser,name='signup'),
    url(r'login/$',views.login,name='login'),
    url(r'^index/$',views.mainindex,name='index'),
    url(r'^logout/$',logout_then_login,{'login_url':'/site/'},name='logout'),
    url(r'^tool/(\d+)/$',views.toolsindex,name='toolpage'),
    url(r'^download/(\d+)/$',views.download,name='download'),
    url(r'^list/$',views.index,name='list'),
    url(r'^user/$', views.user,name='user'),
    url(r'^user_message/$',views.user_change),
    # url(r'^upheadportrait/$',views.up_head_portrait),
    # url(r'^modify/$',views.modify),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^message',views.indexmessage,name='message'),
    url(r'^m78/$',views.m78),
    url(r'^upload/$',views.upfiles,name='upload'),


]
handler404=views.page_not_found
handler500=views.page_not_found