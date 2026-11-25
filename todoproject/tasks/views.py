# from django.shortcuts import render
# from .models import Task


# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks/task_list.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})