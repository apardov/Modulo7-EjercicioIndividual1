from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
def home(request):
    return render(request, template_name='fenix_store/home.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('authenticated')
            else:
                messages.error(request, message='Usuario o contraseña incorrectos')
    else:
        form = UserLoginForm()
    return render(request, template_name='fenix_store/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def authenticated(request):
    return render(request, template_name='fenix_store/authenticated.html')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Te has registrado correctamente.')
            return render(request, template_name='fenix_store/register.html', context={'form': form})
    else:
        form = UserRegisterForm()
    return render(request, template_name='fenix_store/register.html', context={'form': form})
