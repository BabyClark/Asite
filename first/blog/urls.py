from django.conf.urls import url
from . import views
#import first
import os
import django
app_name = 'blog'
from django.contrib.auth.views import logout_then_login

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index$',views.index,name='index'),
    url(r'^post$',views.post,name='blog'),
    url(r'^life$',views.life,name='life'),
    url(r'^djangojz/$',views.djangojz,name='djangojz'),
    url(r'^movie/$',views.movie,name='movie'),
    url(r'^study/$',views.study,name='study'),
    url(r'^comment/$',views.write_comment,name='comment'),
    url(r"^sitemap", views.sitemap)
]