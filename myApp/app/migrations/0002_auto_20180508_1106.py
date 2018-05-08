# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillmodels',
            name='skill_proficiency',
            field=models.CharField(verbose_name='熟练度', default=0, choices=[('lj', '了解'), ('sl', '熟练'), ('jt', '精通')], max_length=10),
        ),
        migrations.AlterField(
            model_name='skillmodels',
            name='skill_type',
            field=models.CharField(verbose_name='技能类型', default=0, choices=[('android', 'Android'), ('python', 'Python')], max_length=10),
        ),
    ]
