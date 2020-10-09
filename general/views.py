from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from  django.http import HttpResponse


def index(request):
    return render(request, 'general/index.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_all')
    form = TaskForm()
    contexct = {'form': form}
    return render(request, 'general/create.html', contexct)


def tasks_all(request):
    tasks = Task.objects.all()
    return render(request, 'general/tasks_all.html', {'tasks': tasks})

# Create your views here.
