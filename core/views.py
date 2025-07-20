from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardResultsSetPagination
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Project, Task, SubTask, Tag, TaskTag, Comment, Attachment, Reminder, ActivityLog
from .forms import TaskForm
from .models import *
from .serializers  import*
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from rest_framework.renderers import JSONRenderer
from django.contrib import messages




# list projects
class ProjectListView(LoginRequiredMixin, View):
    def get(self, request):
        projects = Project.objects.filter(user=request.user).order_by('id')
        paginator = Paginator(projects, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'dashboard/projects_list.html', {'page_obj': page_obj})

# List all tasks in a project
class TaskListView(LoginRequiredMixin, View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id, user=request.user)
        tasks = project.tasks.all().order_by('id')
        paginator = Paginator(tasks, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'dashboard/tasks_list.html', {'project': project, 'page_obj': page_obj})

# create a new Task
class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request, project_id):
        form = TaskForm()
        project = get_object_or_404(Project, id=project_id, user=request.user)
        return render(request, 'forms/task_form.html', {'form': form, "project": project})
    
    def post(self, request, project_id):
        form = TaskForm(request.POST)
        project = get_object_or_404(Project, id=project_id, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.user = request.user
            task.save()
            messages.success(request, 'Task Created Successfully')
            return redirect('tasks-list', project_id=project.id)
        messages.error(request, "Task not created-Failed!")
        return render(request, 'forms/task_form.html', {'form': form, 'project': project})











   
# api >> viewsets

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    # renderer_classes = [JSONRenderer]
    pagination_class = StandardResultsSetPagination
    
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend]
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['user', 'priority', 'is_completed', 'due_date']
    search_fields = ['title', 'description']
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return super().get_queryset().filter(task__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return super().get_queryset().filter(task__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return super().get_queryset().filter(task__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return super().get_queryset().filter(task__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

class TaskTagViewSet(viewsets.ModelViewSet):
    queryset = TaskTag.objects.all()
    serializer_class = TaskTagSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return super().get_queryset().filter(task__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
        
class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

