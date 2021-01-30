from django.urls import path, include
from . import views
from .views import TasksAll, CreateTask, Update, HistoryTasks

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', CreateTask.as_view(), name='create'),
    path('tasks_all/', TasksAll.as_view(), name='tasks_all'),
    path('tasks_all/<int:pk>/update/', Update.as_view(), name='update'),
    path('auth_user/', include('auth_app.urls')),
    path('history/', HistoryTasks.as_view(), name='history'),

]