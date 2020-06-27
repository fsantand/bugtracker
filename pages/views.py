from django.shortcuts import render
from apps.project.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    ctx = {
        'projects':projects
    }
    return render(request, 'index.html', ctx)
    