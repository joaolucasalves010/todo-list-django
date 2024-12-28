# urls.py
from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create'),
    path('finish/', views.finish_task, name='finish'),
    path('delete/', views.delete_task, name='delete'),
]
