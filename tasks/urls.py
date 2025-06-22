from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tasks' # as a namespace for reverse function or reverse_lazy function for urls

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks_list, name='list'),
    path('tasks/<int:id>/', views.task_detail, name = 'detail'),
    path('tasks/create/', views.task_create, name = 'create'),
    path('tasks/<int:id>/update/', views.task_update, name='update'),
    path('tasks/<int:id>/delete/', views.task_delete, name='delete'),
]
