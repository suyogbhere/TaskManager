from django.contrib import admin
from taskapp.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display =['title','description','due_date']