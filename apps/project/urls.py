from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.ProjectDetail.as_view() , name='project'),
    path('<int:pk>/report', views.ReportBug.as_view() , name='report-bug'),
    path('<int:project>/bug/<int:bug_number>', views.BugThread.as_view(), name='bug-thread'),
]