from django.urls import path, re_path
from . import views


urlpatterns = [
    path('todos/new/', views.task_new, name='task_new'),
    re_path(r'^todos/change_mark/(\d+)/', views.mark_change, name='mark_change'),
    re_path(r'^todos/completed/', views.completed, name='show_completed'),
    path('todos/', views.show_incompleted, name='show_incompleted'),
    path('todos/list_delete', views.list_delete, name='list_delete'),
    re_path(r'^todos/update_task/(\d+)/', views.update_task, name='update_task'),
    re_path(r'^todos/delete_task/(\d+)/', views.delete_task, name='delete_task'),



]