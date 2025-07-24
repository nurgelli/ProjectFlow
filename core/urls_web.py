from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleDoneView,  home_view )


urlpatterns = [
    path('', home_view, name='home'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('projects/add/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:id>/edit/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:id>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    
    
    
    path('projects/<int:project_id>/tasks/', TaskListView.as_view(), name='tasks-list'),
    path('projects/<int:project_id>/tasks/add/', TaskCreateView.as_view(), name='task-create'),
    
    path('projects/<int:project_id>/tasks/<int:task_id>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('projects/<int:project_id>/tasks/<int:task_id>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('projects/<int:project_id>/tasks/<int:task_id>/toggle/', TaskToggleDoneView.as_view(), name='task-toggle'),
    
    # 
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name="components/login.html"), name='login'),
    path('accounts/logout/', auth_views.LoginView.as_view(), name='logout'),
]

