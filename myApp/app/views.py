from django.shortcuts import render
from .models import UserModels, ProjectModels


# Create your views here.

def main(request):
    user = UserModels.objects.all()[0]
    project = ProjectModels.objects.all()
    return render(request, 'app/main.html', {'user': user, 'project': project})
