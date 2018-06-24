# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDjangoUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('des', models.CharField(max_length=50, default=None, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('tools_sum', models.IntegerField(default=0)),
                ('school', models.CharField(max_length=30, null=True)),
                ('subject', models.CharField(max_length=30, null=True)),
                ('head_portrait', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tool_name', models.CharField(max_length=10)),
                ('user', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=10, null=True)),
                ('size', models.IntegerField(null=True)),
                ('belong_to', models.ForeignKey(related_name='tool_message', to='myweb.MyDjangoUser')),
            ],
        ),
    ]
