from django.urls import path, re_path
from main import views


urlpatterns = [
    path('', views.hello),
    path('todos/', views.display),
    path('todos/1/completed/', views.completed),
]
