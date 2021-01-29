from django.urls import path, include
from . import views
from .views import Tasks_all, CreateTask, Update, History_tasks

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', CreateTask.as_view(), name='create'),
    path('tasks_all/', Tasks_all.as_view(), name='tasks_all'),
    path('tasks_all/<int:pk>/update/', Update.as_view(), name='update'),
    path('auth_user/', include('auth_app.urls')),
    path('history/', History_tasks.as_view(), name='history'),

]