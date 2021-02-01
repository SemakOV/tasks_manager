from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from .filter import FilterTasksState


def index(request):
    return render(request, 'general/index.html')


class CreateTask(CreateView):
    form_class = TaskForm
    template_name = 'general/create.html'
    success_url = reverse_lazy('tasks_all')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateTask, self).form_valid(form)

# def create(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             # form.author = request.user.pk
#             form.save()
#             return redirect('tasks_all')
#     form = TaskForm()
#     contexct = {'form': form,
#                 }
#     return render(request, 'general/create.html', contexct)


class Update(UpdateView):
    model = Task
    template_name = 'general/update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks_all')


class TasksAll(ListView):
    model = Task
    template_name = 'general/tasks_all.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksAll, self).get_context_data(**kwargs)
        context['title'] = 'Задачи'
        context['user_pk'] = self.request.user.pk
        context['filter'] = FilterTasksState(self.request.GET, queryset=self.get_queryset())
        return context

# def tasks_all(request):
#     tasks = Task.objects.all()
#     return render(request, 'general/tasks_all.html', {'tasks': tasks,})


class HistoryTasks(TasksAll):
    model = Task
    template_name = 'general/history.html'
    context_object_name = 'tasks'


class FilterTasks(TasksAll):
    model = Task
    template_name = 'general/filter.html'
    context_object_name = 'tasks'


class FilterState(TasksAll):
    model = Task
    template_name = 'general/filter.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(TasksAll, self).get_context_data(**kwargs)
        context['filter'] = FilterTasksState(self.request.GET, queryset=self.get_queryset())
        return context







# class FilterTasksState(django_filters.FilterSet):
#     class Meta:
#         model = Task
#         fields = ('state', )

    #
    # queryset = Task.objects.all()
    # model = Task
    # template_name = 'general/filter.html'
    # context_object_name = 'tasks'
    # filter_backends = [DjangoFilterBackend]






# Create your views here.
