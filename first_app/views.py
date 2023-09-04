from django.shortcuts import render, redirect
from first_app.forms import TaskStoreForm
from first_app.models import TaskStoreModel
# Create your views here.


# Create your views here.


def home(request):
    return render(request, 'store_task.html')


def store_task(request):
    if request.method == 'POST':
        task = TaskStoreForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('show_task')
    else:
        task = TaskStoreForm()
    return render(request, 'store_task.html', {'form': task})


def show_task(request):
    task = TaskStoreModel.objects.all()
    print(task)
    return render(request, 'show_task.html', {'data': task})
