from django import forms
from django.forms import ModelForm
from .models import Task, Task_list

class TaskForm(ModelForm):
    # Class Meta is used for determining what model is used in creation of form
    class Meta:
        model = Task
        fields = ('task_name', 'created_date', 'finished_date',  'owner', 'mark')


