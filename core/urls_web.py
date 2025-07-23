from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (ProjectListView, ProjectCreateView, TaskListView, TaskCreateView)


urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('projects/add', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:project_id>/tasks', ProjectCreateView.as_view(), name='tasks-list'),
    path('projects/<int:project_id>/tasks/add', ProjectCreateView.as_view(), name='task-create'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="components/login.html")),
    path('accounts/logout/', auth_views.LoginView.as_view(), name='logout'),
]

