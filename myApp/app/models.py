from django.db import models


# Create your models here.

class UserModels(models.Model):
    image = models.ImageField(upload_to="user/%Y/%m", verbose_name=u"Logo", max_length=100)
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄', default=0)
    iphone = models.CharField(max_length=11, verbose_name='电话')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    message = models.CharField(max_length=500, verbose_name='个人简介')

    class Meta:
        db_table = 'user'


class ProjectModels(models.Model):
    image = models.ImageField(upload_to="project/%Y/%m", verbose_name=u"Logo", max_length=100)
    test = models.CharField(max_length=500, verbose_name='项目简介')
    url = models.CharField(max_length=500, verbose_name='项目路径')

    class Meta:
        db_table = 'project'
