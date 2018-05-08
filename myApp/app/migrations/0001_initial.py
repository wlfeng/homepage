# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModels',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20, verbose_name='公司名称')),
                ('company_image', models.ImageField(upload_to='company/%Y/%m')),
                ('start_time', models.DateField(verbose_name='入职时间')),
                ('end_time', models.DateField(verbose_name='离职时间')),
            ],
            options={
                'verbose_name_plural': '工作公司',
                'verbose_name': '工作公司',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='ProjectModels',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/%Y/%m', verbose_name='Logo')),
                ('test', models.CharField(max_length=500, verbose_name='项目简介')),
                ('url_image', models.ImageField(upload_to='url_image/%Y/%m', verbose_name='Logo')),
                ('name', models.CharField(max_length=20, verbose_name='项目名称')),
            ],
            options={
                'verbose_name_plural': '项目经验',
                'verbose_name': '项目经验',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='SkillModels',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('skill_type', models.CharField(max_length=10, default=0, verbose_name='技能类型', choices=[(0, 'Android'), (1, 'Python')])),
                ('skill_test', models.CharField(max_length=200, verbose_name='技能')),
                ('skill_proficiency', models.CharField(max_length=10, default=0, verbose_name='熟练度', choices=[(0, '了解'), (1, '熟练'), (2, '精通')])),
            ],
            options={
                'verbose_name_plural': '技能',
                'verbose_name': '技能',
                'db_table': 'Skill',
            },
        ),
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user/%Y/%m', verbose_name='Logo')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('iphone', models.CharField(max_length=11, verbose_name='电话')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('message', models.CharField(max_length=500, verbose_name='个人简介')),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='WorkModels',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('work', models.CharField(max_length=100, verbose_name='工作职责')),
                ('company', models.ForeignKey(to='app.CompanyModels', verbose_name='公司')),
            ],
            options={
                'verbose_name_plural': '工作职责',
                'verbose_name': '工作职责',
                'db_table': 'work',
            },
        ),
    ]
