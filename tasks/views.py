from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    return render(request, 'tasks/pages/index.html', contenxt = {'index': index})

def tasks_list(request):
    task = Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': task})

def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    return render(request, 'tasks/task_create.html', {"form": form})

def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', id=task.id)
    return render(request, 'tasks/task_create.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('tasks_list')
    return render(request, 'tasks/confirm.html', {"task": task})                                                                                                                                                                                                                      