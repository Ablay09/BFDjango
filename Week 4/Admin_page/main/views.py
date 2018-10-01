from django.shortcuts import render
from django.http import HttpResponse

import datetime
from datetime import timedelta

now = datetime.datetime.now()
dt = now + timedelta(3)


def display(request):
    todo_list = [{
            'task': "Task {}".format(i),
            'created': now.strftime('%d/%m/%Y'),
            'due_on': dt.strftime('%d/%m/%Y'),
            'owner': "admin",
            'mark': False
        }
        for i in range (1,5)
    ]
    context = {
            'todo_list' : todo_list,
    }
    return render(request, 'todo_list.html', context)
def completed(request):
    completed_list = [{
        'task': "Task {}".format(j),
        'created': now.strftime('%d/%m/%Y'),
        'due_on': dt.strftime('%d/%m/%Y'),
        'owner': "admin",
        'mark': False
        }
        for j in range(1)
    ]

    context = {
        'completed_list': completed_list
    }
    return render(request, 'completed_todo_list.html', context)

def hello(request):
    return HttpResponse("Hello, macho ))")

