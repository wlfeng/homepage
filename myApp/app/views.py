from django.shortcuts import render
from .models import UserModels, ProjectModels, CompanyModels, SkillModels


# Create your views here.

def main(request):
    user = UserModels.objects.all()[0]
    project = ProjectModels.objects.all()
    company = CompanyModels.objects.all()
    skill = SkillModels.objects.all()
    android = skill.filter(skill_type='android')
    python = skill.filter(skill_type='python')
    return render(request, 'app/index.html',
                  {'user': user, 'project': project, 'company': company, 'android': android, 'python': python})
