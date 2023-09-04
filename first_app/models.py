from django.db import models

# Create your models here.


class TaskStoreModel(models.Model):
    id = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=30)
    task_description = models.CharField(max_length=130)
    is_completed = models.BooleanField(default=False)
    first_pub = models.DateTimeField()
    last_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle
