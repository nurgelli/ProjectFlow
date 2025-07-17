from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import *

router = DefaultRouter()

router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('subtasks', SubTaskViewSet)
router.register('tags', TagViewSet)
router.register('tasktags', TaskTagViewSet)
router.register('comments', CommentViewSet)
router.register('attachments', AttachmentViewSet)
router.register('reminders', ReminderViewSet)
router.register('activitylogs', ActivityLogViewSet)

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('projects/<int:project_id>/tasks/', TaskListView.as_view(), name='tasks-list'),
    path('projects/<int:project_id>/tasks/add/', TaskCreateView.as_view(), name='task-create'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login.html'), name='logout'),
    path('', include(router.urls)), 
]

