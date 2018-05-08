from django.contrib import admin
from .models import UserModels, ProjectModels,WorkModels,CompanyModels,SkillModels

# Register your models here.
admin.site.register(UserModels)
admin.site.register(ProjectModels)
admin.site.register(WorkModels)
admin.site.register(CompanyModels)
admin.site.register(SkillModels)
