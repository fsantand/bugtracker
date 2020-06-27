from django.shortcuts import render
from django.views.generic import DetailView, CreateView, TemplateView

from .models import Project
from apps.bug.models import Bug

# Create your views here.
class ProjectDetail(DetailView):
    model = Project

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

    def get_context_data(self, **kwargs):
        bug = Bug.objects.get(project__pk = self.kwargs['project'], bug_number = self.kwargs['bug_number'])
        ctx = {
            'bug': bug
        }
        return ctx
        
