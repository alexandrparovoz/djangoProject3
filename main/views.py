from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, DetailView, UpdateView

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail_view.html'
    context_object_name = 'article'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'create.html'
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = 'task_detail'
    template_name = 'deletetask.html'


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def add_task(request):
    return render(request, 'main/addtask.html')

def edit_task(request):
    tasks = Task.objects.all()
    return render(request, 'main/edittask.html', {'tasks': tasks})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/edittask')
        else:
            error = 'Форма заполнена некорректно!'
    form = TaskForm()
    context = {
        'form': form,
        'error': error

    }
    return render(request, 'main/create.html', context)
