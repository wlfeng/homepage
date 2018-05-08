# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180508_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillmodels',
            name='skill_proficiency',
            field=models.CharField(max_length=10, default='jt', verbose_name='熟练度', choices=[('lj', '了解'), ('sl', '熟练'), ('jt', '精通')]),
        ),
        migrations.AlterField(
            model_name='skillmodels',
            name='skill_type',
            field=models.CharField(max_length=10, default='python', verbose_name='技能类型', choices=[('android', 'Android'), ('python', 'Python')]),
        ),
    ]
