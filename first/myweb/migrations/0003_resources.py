# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_remove_tools_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='resources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=10)),
                ('size', models.IntegerField(null=True)),
                ('belong_to', models.ForeignKey(to='myweb.MyDjangoUser', related_name='resouce_message')),
            ],
        ),
    ]
