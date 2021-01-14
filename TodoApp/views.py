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

