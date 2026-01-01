from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            user=request.user
        )
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            user=request.user
        )
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

