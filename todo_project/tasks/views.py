from django.shortcuts import render, redirect
from .models import Task
from .forms import *


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'home.html', context)


def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('Form is invalid')

    context = {'form': form}
    return render(request, 'create.html', context)


def detail_task(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'detail.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('Form is invalid')

    context = {'form': form}
    return render(request, 'update.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')
    context = {'task': task}
    return render(request, 'delete.html', context)