from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class HelloView(LoginRequiredMixin, ListView):
    template_name = 'tasks/hello.html'

class WelcomeView(LoginRequiredMixin, ListView):
    template_name = 'tasks/welcome.html'

def home(request):
    return render(request, 'tasks/home.html')

    




