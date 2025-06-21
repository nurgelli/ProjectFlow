from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.tasks_list, name='tasks_list'),
    path('tasks/<int:id>/', views.task_detail, name = 'task_detail'),
    path('tasks/create/', views.task_create, name = 'task_create'),
    path('tasks/<int:id>/update/', views.task_update, name='task_update'),
    # path('<int:id>/delete/', views.task_delete, name='task_delete'),
]
