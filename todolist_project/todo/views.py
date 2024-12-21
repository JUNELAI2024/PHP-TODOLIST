
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    """Display the list of tasks."""
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    """Handle task creation."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list after saving
    else:
        form = TaskForm()  # Create an empty form for GET requests
    
    return render(request, 'todo/add_task.html', {'form': form})  # Render the form templateorm})