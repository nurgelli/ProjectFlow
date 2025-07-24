from django import forms
from .models import Project, Task, SubTask, Comment, Attachment, Reminder


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ["name", "description", "color"]
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'priority': forms.Select(),
        }
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        