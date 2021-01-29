from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


def user_logout(request):
     logout(request)
     return redirect('auth_user')


def auth(request):
     if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
               user = form.get_user()
               login(request, user)
               return redirect('home')

     form = AuthenticationForm()
     return render(request, 'auth_app/auth_app.html', {'form': form})


def registration(request):
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)

          if form.is_valid():
               user = form.save()
               login(request, user)
               # messages.success(request, "Вы зарегистрированы")
               return redirect('home')

     form = UserRegisterForm()
     return render(request, 'auth_app/registration.html', {'form': form})



# Create your views here.
