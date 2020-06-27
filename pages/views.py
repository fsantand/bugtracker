from django.shortcuts import render
from apps.project.models import Project
from apps.bug.models import Bug

# Create your views here.
def index(request):
    projects = Project.objects.all()
    bugs = Bug.objects.all()
    ctx = {
        'projects':projects,
        'bugs':bugs
    }
    return render(request, 'index.html', ctx)
    