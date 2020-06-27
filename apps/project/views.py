from django.shortcuts import render
from django.views.generic import DetailView, CreateView

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