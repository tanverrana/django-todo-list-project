from django.shortcuts import render, redirect
from first_app.forms import TaskStoreForm
from first_app.models import TaskStoreModel
# Create your views here.


# Create your views here.


def home(request):
    if request.method == 'POST':
        task = TaskStoreForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('show_task')
    else:
        task = TaskStoreForm()
    return render(request, 'store_task.html', {'form': task})


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


def edit_task(request, id):
    task = TaskStoreModel.objects.get(pk=id)
    form = TaskStoreForm(instance=task)
    if request.method == 'POST':
        form = TaskStoreForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    return render(request, 'store_task.html', {'form': form})


def delete_task(request, id):
    task = TaskStoreModel.objects.get(pk=id).delete()
    return redirect('show_task')
