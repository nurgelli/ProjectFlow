from django.shortcuts import render
from tasks.models import Task


# Create your views here.

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {"tasks": tasks})
