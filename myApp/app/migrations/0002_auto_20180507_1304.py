# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='projectmodels',
            table='project',
        ),
        migrations.AlterModelTable(
            name='usermodels',
            table='user',
        ),
    ]
