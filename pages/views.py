from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView, LogoutView
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

class UserLogin(LoginView):
    template_name = 'registration/login.html'
    next = 'index'
    
class UserLogout(LogoutView):
    next_page = 'index'