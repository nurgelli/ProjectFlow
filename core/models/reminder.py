from django.db import models
from .task import Task


class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reminders")
    remind_at = models.DateTimeField()
    sent = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.task.title} - Reminder at {self.remind_at.strftime("%Y-%m-%d %H:%M:%S")}'