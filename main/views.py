from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        # Osea que esta logeado
        return redirect('index')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}')
                return redirect('index')
            else:
                messages.warning(request, 'No te haz logeado correctamente')

        return render(request, 'auth/login.html')

def register_page(request):
    if request.user.is_authenticated:
        # Osea que esta logeado
        return redirect('index')
    else:

        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Te has registrado correctamente')
                form.save()
                return redirect('register')

        return render(request, 'auth/register.html', {
            'form': form
        })


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')