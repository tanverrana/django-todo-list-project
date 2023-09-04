from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from first_app.forms import TaskStoreForm

# Create your views here.


def home(request):
    return render(request, 'store_task.html')


def store_task(request):
    task = TaskStoreForm(request.POST)
    print(task)
    return render(request, 'store_task.html', {'form': task})
