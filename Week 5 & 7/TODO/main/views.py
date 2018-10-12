from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse

import datetime
from datetime import timedelta
from .forms import TaskForm
from .models import Task, Task_list

now = datetime.datetime.now()
dt = now + timedelta(3)

def completed(request):
    completed_list = [i for i in Task.objects.all() if i.mark]
    context = {
        'completed_list': completed_list
    }
    return render(request, 'completed_todo_list.html', context)

def show_incompleted(request):
    incompleted_list = Task.objects.all().filter(mark=False)
    print(incompleted_list)
    context = {
        'incompleted_list': incompleted_list
    }
    return render(request, 'todo_list.html', context)

def list_delete(request):
    Task.objects.all().delete()
    return redirect('show_incompleted')

def mark_change(request, id):
    task = Task.objects.get(pk=id)
    if task.mark:
        task.mark = False
    else:
        task.mark = True
    task.save()
    return redirect('show_incompleted')

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_incompleted')
    else:
        form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'Task/task_form.html', context)

def update_task(request, id):
    updated = get_object_or_404(Task, pk=id)
    form = TaskForm(request.POST or None, instance=updated)
    if form.is_valid():
        form.save()
        return redirect('show_incompleted')
    return render(request, 'Task/task_form.html', {'form': form})


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_incompleted')


