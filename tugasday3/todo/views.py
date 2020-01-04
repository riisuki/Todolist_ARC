from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm, NewTodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('due')
    #form = TodoForm()
    newtodoform = NewTodoForm()

    context = {'todo_list' : todo_list, 'form' : newtodoform}
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    #form = TodoForm(request.POST)
    newtodoform = NewTodoForm(request.POST)
    
    if newtodoform.is_valid():
        #new_todo = Todo(text=request.POST['text']) #new_todo = Todo(text=form.cleaned_data['text'])
        #new_todo.save()
        new_todo = newtodoform.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.complete:
        todo.complete = False
    else:
        todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteItem(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')

def editItem(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    text = todo.text
    desc = todo.desc
    due = todo.due
    return

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')

def remove(request, item_id): 
    item = Todo.objects.get(id=item_id) 
    item.delete() 
    return redirect('index') 