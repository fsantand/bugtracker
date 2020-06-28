from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project
from apps.bug.models import Bug, Comment

# Create your views here.
class ProjectDetail(DetailView):
    model = Project

class ProjectCreate(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['name', 'short_description']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ReportBug(CreateView):
    model = Bug
    template_name = "project/report_bug.html"
    fields = [
        'title',
        'classification',
        'description'
    ]

    def get_context_data(self, **kwargs):
        self.user = self.request.user
        self.project = Project.objects.get(pk = self.kwargs['pk'])
        ctx = super(ReportBug, self).get_context_data(**kwargs)
        ctx['user'] = self.user
        ctx['project'] = self.project
        return ctx

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk = self.kwargs['pk'])
        form.instance.reporter = self.request.user
        form.instance.bug_number = form.instance.project.get_bug_num()
        return super().form_valid(form)

class BugThread(TemplateView):
    template_name = 'bug/bug_detail.html'

    def post(self, request, project, bug_number):
        bug = Bug.objects.get(project__pk = project, bug_number = bug_number)
        comm = Comment(
            bug = bug,
            commenter = request.user,
            comment = request.POST['comment']
        )
        if 'close_thread' in request.POST.keys():
            close_thread = request.POST['close_thread']
            print(close_thread)
            if close_thread:
                bug.close_bug()
                print(f'The bug {bug} is now closed.')
        comm.save()
        return redirect('bug-thread', project, bug_number)

    def get_context_data(self, **kwargs):
        bug = Bug.objects.get(project__pk = self.kwargs['project'], bug_number = self.kwargs['bug_number'])
        ctx = {
            'bug': bug
        }
        return ctx
        
