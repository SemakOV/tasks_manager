from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth_user'),
    path('registration', views.registration, name='registration'),
    path('user_logout', views.user_logout, name='user_logout')

]