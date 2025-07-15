from django.db import models
from django.contrib.auth import get_user_model
from .project import Project



User = get_user_model()


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("med", "Medium"),
        ("high", "High"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="med")
    due_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_recurring = models.BooleanField(default=False)
    recurrence_pattern = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.title