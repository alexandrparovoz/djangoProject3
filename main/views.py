from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    if request.method == 'post':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
