from django.shortcuts import render, redirect
from .models import Todo
from .form import FormTodo
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def todo(request):
    if request.method == 'POST':
        form = FormTodo(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

    todos = Todo.objects.filter(user=request.user)
    context = {
        'todos': todos
    }
    return render(request, 'task.html', context)


@login_required(login_url='login')
def delete(request, id):
    todos = Todo.objects.get(id=id)
    todos.delete()
    return redirect('todo')
