from django.contrib import admin
from todo import models

# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
  list_display=('id', 'task_name')
  ordering=('id',)