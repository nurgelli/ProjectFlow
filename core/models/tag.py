from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    
    
    def __str__(self):
        return (f"{self.name} > {self.user}")
    
class TaskTag(models.Model):
    task = models.ForeignKey('core.Task', on_delete=models.CASCADE) # I will return later, bashga
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    
    class Meta:
        unique_together = ("task", "tag")
        
    def __str__(self):
        return self.tag.name
        