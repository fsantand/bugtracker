from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', include('apps.project.urls')),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('logout/', views.UserLogout.as_view(), name="logout"),
]
