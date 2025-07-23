from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProjectViewSet, TaskViewSet, 
                    SubTaskViewSet, TagViewSet, TaskTagViewSet,
                    CommentViewSet, AttachmentViewSet,
                    ReminderViewSet, ActivityLogViewSet)

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
    path('', include(router.urls)), 
]

