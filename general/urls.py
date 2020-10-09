from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('tasks_all', views.tasks_all, name='tasks_all'),
    path('auth_user/', include('auth_app.urls'))

]