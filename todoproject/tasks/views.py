# from django.shortcuts import render
# from .models import Task


# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks/task_list.html', {'tasks': tasks})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# def task_list(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()

#     tasks = Task.objects.all()
#     return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    done_count = tasks.filter(is_completed=True).count()
    pending_count = tasks.filter(is_completed=False).count()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'form': form,
        'done_count': done_count,
        'pending_count': pending_count,
    })


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_edit.html', {'form': form, 'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_delete.html', {'task': task})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
    return redirect('task_list')