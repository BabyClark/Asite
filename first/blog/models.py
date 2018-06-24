from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class MyBlogUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(null=True)
    des=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.user.username
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created =MyBlogUser.objects.get_or_create(user=instance)
post_save.connect(create_user_profile, sender=User)


class artical(models.Model):
    writer=models.CharField(max_length=20)
    title=models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    viewtimes=models.IntegerField(default=0)
    text=models.TextField(max_length=80000)
    subject=models.CharField(max_length=10)
    abstract=models.TextField(max_length=3000)
    commment_times=models.IntegerField(default=0)
    def __str__(self):
        return self.title

class comment(models.Model):
    #user=models.ForeignKey(to=MyBlogUser,related_name='user',on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now_add=True)
    text=models.CharField(max_length=500)
    belong_to=models.ForeignKey(to=artical,related_name='comment_message',on_delete=models.CASCADE)

class artical_count(models.Model):
    movienum=models.IntegerField(default=0)
    lifenum=models.IntegerField(default=0)
    djangojznum=models.IntegerField(default=0)
    studynum=models.IntegerField(default=0)