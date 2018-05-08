# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', models.ImageField(verbose_name='项目图片', upload_to='')),
                ('test', models.CharField(max_length=500, verbose_name='项目简介')),
                ('url', models.CharField(max_length=500, verbose_name='项目路径')),
            ],
        ),
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', models.ImageField(verbose_name='头像', upload_to='')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('iphone', models.CharField(max_length=11, verbose_name='电话')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('message', models.CharField(max_length=500, verbose_name='个人简介')),
            ],
        ),
    ]
