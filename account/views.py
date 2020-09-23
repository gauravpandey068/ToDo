from django.shortcuts import render, redirect
from .forms import CreateUserForm, EditUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.user.is_authenticated:
        return redirect('todo')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo')
            else:
                messages.info(request, "UserName or Password not Match")
                return render(request, 'login.html')
        context = {

        }
        return render(request, 'login.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('todo')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was Created!')
                return redirect('todo')

        context = {
            'form': form

        }
        return render(request, 'signup.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated!')
            return redirect('todo')

    users = User.objects.get(first_name=request.user.first_name, last_name=request.user.last_name,
                             email=request.user.email)
    context = {
        'users': users

    }
    return render(request, 'profile.html', context)
