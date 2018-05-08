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
        verbose_name = verbose_name_plural = '用户'

    def __str__(self):
        return self.name


class ProjectModels(models.Model):
    image = models.ImageField(upload_to="project/%Y/%m", verbose_name=u"Logo", max_length=100)
    test = models.CharField(max_length=500, verbose_name='项目简介')
    url_image = models.ImageField(upload_to="url_image/%Y/%m", verbose_name=u"Logo", max_length=100)
    name = models.CharField(max_length=20, verbose_name='项目名称')

    class Meta:
        db_table = 'project'
        verbose_name = verbose_name_plural = '项目经验'

    def __str__(self):
        return self.name


class CompanyModels(models.Model):
    company_name = models.CharField(max_length=20, verbose_name='公司名称')
    company_image = models.ImageField(upload_to="company/%Y/%m", max_length=100)
    start_time = models.DateField(verbose_name='入职时间')
    end_time = models.DateField(verbose_name='离职时间')

    class Meta:
        db_table = 'company'
        verbose_name = verbose_name_plural = '工作公司'

    def __str__(self):
        return self.company_name


class WorkModels(models.Model):
    company = models.ForeignKey(CompanyModels, verbose_name='公司')
    work = models.CharField(max_length=100, verbose_name='工作职责')

    class Meta:
        db_table = 'work'
        verbose_name = verbose_name_plural = '工作职责'

    def __str__(self):
        return self.work


class SkillModels(models.Model):
    skill_type = models.CharField(max_length=10, choices=(('android', 'Android'), ('python', 'Python')),
                                  default='python',
                                  verbose_name='技能类型')
    skill_test = models.CharField(max_length=200, verbose_name='技能')
    skill_proficiency = models.CharField(max_length=10, choices=(('lj', '了解'), ('sl', '熟练'), ('jt', '精通')),
                                         default='jt',
                                         verbose_name='熟练度')

    class Meta:
        db_table = 'Skill'
        verbose_name = verbose_name_plural = '技能'

    def __str__(self):
        return self.skill_test
