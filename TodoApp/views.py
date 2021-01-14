from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

class IndexView(View):
    def get(self, request):
        tasks = Task.objects.all()
        form = TaskForm()

        context = {'tasks':tasks, 'form':form}

        return render(request, 'TodoApp/index.html', context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')


class UpdateView(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        form = TaskForm(instance=task)

        context = {'form':form}

        return render(request, 'TodoApp/update.html', context)

    def post(self, request, id):
        task = Task.objects.get(id=id)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect('/')

