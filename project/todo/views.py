# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if tasks:
        context = {'tasks': tasks, 'class': 'show'}
    else:
        context = {'class': 'hide'}
    return render(request, 'todo/index.html', context)

def create_task(request):
    if request.method == "POST":
        task_name = request.POST.get("task_name")
        if task_name:
            new_task = Task(task_name=task_name)
            new_task.save()
            return redirect('todo:index')
    return render(request, 'todo/index.html')

def finish_task(request):
    if request.method == "POST":
        id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=id)
        task.finished = True
        task.save()
        return redirect('todo:index')

def delete_task(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        if task_id:
            task = Task.objects.filter(id=task_id)
            task.delete()
            return redirect('todo:index')
    return render(request, 'todo/index.html')