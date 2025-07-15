from django.db import models
from django.contrib.auth import get_user_model
from .task import Task

User = get_user_model()

class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('completed', 'Completed'),
        ('deleted', 'Deleted'),
        ('commented', 'Commented'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.action
