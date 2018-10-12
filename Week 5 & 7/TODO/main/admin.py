from django.contrib import admin
from .models import Task, Task_list


admin.site.register(Task)

@admin.register(Task_list)
class TaskListAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'time')
