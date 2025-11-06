from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    """
    Vista para mostrar todas las tareas y manejar la creación de una nueva tarea.
    """
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def task_detail(request, pk):
    """
    Vista para mostrar los detalles de una tarea específica.
    """
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_update(request, pk):
    """
    Vista para actualizar una tarea existente.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})

def task_delete(request, pk):
    """
    Vista para eliminar una tarea.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_delete.html', {'task': task})
