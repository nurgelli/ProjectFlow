from django.contrib import admin
from .models import (Project, Task, SubTask, Tag, TaskTag, Comment, Attachment, Reminder, ActivityLog)
# Register your models here.

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    
class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1
class ReminderInline(admin.TabularInline):
    model = Reminder
    extra = 1 

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1    
    


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', "description")
    list_filter = ("created_at",)
    ordering = ('-created_at',)
    # inlines = [TaskInline]
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'user', 'priority', 'due_date', 'is_completed')
    search_fields = ('title', 'priority', 'description')
    list_filter = ('priority', 'is_completed', 'created_at', 'user')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [SubTaskInline, CommentInline, AttachmentInline, ReminderInline ]

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'title', 'is_completed', 'order')
    list_filter = ('is_completed',)
    search_fields = ('title',)
    ordering = ('order',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    search_fields = ('name',)


@admin.register(TaskTag)
class TaskTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'tag')
    search_fields = ('task__title', 'tag__name')
    list_filter = ('tag',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'content', 'created_at')
    search_fields = ('content',)
    readonly_fields = ('created_at',)
    
@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'file', 'uploaded_at')
    search_fields = ('task__title',)
    readonly_fields = ('uploaded_at',)
    
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'remind_at', 'sent')
    list_filter = ('sent',)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'timestamp')
    search_fields = ('note', 'action')
    list_filter = ('timestamp',)
    readonly_fields = ('timestamp',)
     
    
    

