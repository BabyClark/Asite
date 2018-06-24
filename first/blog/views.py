from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
from .models import artical_count
from django.core.paginator import Paginator
def index(request):
    countnum=artical_count.objects.all().get(id=1)
    # limit = 6
    # simple = artical.objects.all()
    # page_data = Paginator(simple, limit)
    # page_way = request.GET.get('page', 1)
    # load = page_data.page(page_way)
    first=artical.objects.all().get(id=10)
    load=artical.objects.order_by('-time').all().exclude(id=10)
    time_list = artical.objects.order_by('-time').filter()
    time_list=time_list[0:3]
    comm = comment.objects.order_by('-time').filter()
    comm=comm[0:3]
    con = {
        'first':first,
        'time_list':time_list,
        'obs': load,
        'count': countnum,
        'com':comm
    }
    return render(request,'blog/indexfirst.html',con)

def post(request):
    countnum = artical_count.objects.all().get(id=1)
    artic=request.GET.get('page')
    simple = artical.objects.all().get(id=artic)
    comm=comment.objects.all().filter(belong_to=simple)
    time_list = artical.objects.order_by('-time').filter()
    time_list = time_list[0:3]
    con = {
        'count': countnum,
        'time_list':time_list,
        'obs': simple,
        'com':comm,
    }
    return render(request,'blog/post.html',con)

def life(request):
    countnum = artical_count.objects.all().get(id=1)
    load = artical.objects.order_by('-time').filter(subject='生活')
    time_list = artical.objects.order_by('-time').filter()
    time_list = time_list[0:3]
    comm = comment.objects.order_by('-time').filter()
    comm = comm[0:3]
    con={
        'count': countnum,
        'time_list': time_list,
        'obs':load,
        'com': comm
    }
    return render(request, 'blog/index.html', con)

def djangojz(request):
    countnum = artical_count.objects.all().get(id=1)
    load = artical.objects.order_by('-time').filter(subject='django建站')
    time_list = artical.objects.order_by('-time').filter()
    time_list = time_list[0:3]
    comm = comment.objects.order_by('-time').filter()
    comm = comm[0:3]
    con={
        'count': countnum,
        'time_list': time_list,
        'obs':load,
        'com': comm
    }
    return render(request, 'blog/index.html', con)

def movie(request):
    countnum = artical_count.objects.all().get(id=1)
    load = artical.objects.order_by('-time').filter(subject='movie')
    time_list = artical.objects.order_by('-time').filter()
    time_list = time_list[0:3]
    comm = comment.objects.order_by('-time').filter()
    comm = comm[0:3]
    con={
        'count': countnum,
        'time_list': time_list,
        'obs':load,
        'com': comm
    }
    return render(request, 'blog/index.html', con)

def study(request):
    countnum = artical_count.objects.all().get(id=1)
    load = artical.objects.order_by('-time').filter(subject='学习笔记')
    time_list = artical.objects.order_by('-time').filter()
    time_list = time_list[0:3]
    comm = comment.objects.order_by('-time').filter()
    comm = comm[0:3]
    con={
        'count': countnum,
        'time_list': time_list,
        'obs':load,
        'com': comm
    }
    return render(request, 'blog/index.html', con)

from .forms import *
def write_comment(request):
    if request.method=='POST':
        comm=commentform(request.POST)
        if comm.is_valid():
            belong=comm.cleaned_data['belongto']
            art=artical.objects.get(title=belong)
            new_comment=comment(
                name=comm.cleaned_data['name'],
                text=comm.cleaned_data['message'],
                belong_to=art
            )
            new_comment.save()
            art.commment_times+=1
            art.save()
            belong = comm.cleaned_data['belongto']
            return HttpResponseRedirect('/blog/post?page={}'.format(art.id))

def sitemap(request):
    return render(request,'sitemap.xml')