from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class MyDjangoUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    des=models.CharField(max_length=50,default=None,null=True,blank=True)
    email=models.EmailField(null=True)
    tools_sum=models.IntegerField(default=0)
    school=models.CharField(max_length=30,null=True)
    subject=models.CharField(max_length=30,null=True)
    head_portrait=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.user.username
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created =MyDjangoUser.objects.get_or_create(user=instance)
post_save.connect(create_user_profile, sender=User)



class Tools(models.Model):
    tool_name=models.CharField(max_length=30,blank=False,null=False)
    user=models.CharField(max_length=10,blank=False,null=False)
    time=models.DateTimeField(auto_now_add=True)
    subject=models.CharField(max_length=30)
    size=models.IntegerField(null=True)
    belong_to=models.ForeignKey(to=MyDjangoUser,related_name='tool_message',on_delete=models.CASCADE)
    def __str__(self):
        return self.tool_name

class resources(models.Model):
    name=models.CharField(max_length=10,blank=False,null=False)
    time=models.DateTimeField(auto_now_add=True)
    subject=models.CharField(max_length=10)
    size=models.IntegerField(null=True)
    belong_to=models.ForeignKey(to=MyDjangoUser,related_name='resouce_message',on_delete=models.CASCADE)
    def __str__(self):
        return self.name