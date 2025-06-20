from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.task, name='tasks_list'),
    path('<int:id>/', views.task_detail, name = 'task_detail'),
    path('create/', views.task_create, name = 'task_create'),
    path('<int:id>/update/', views.task_update, name='task_update'),
    path('<int:id>/delete/', views.task_delete, name='task_delete'),
]
