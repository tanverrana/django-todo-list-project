from django import forms
from first_app.models import TaskStoreModel


class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskStoreModel
        fields = ['id', 'task_name', 'task_description']
