from django.contrib import admin
from .models import UserModels, ProjectModels

# Register your models here.

admin.site.register(UserModels)
admin.site.register(ProjectModels)
