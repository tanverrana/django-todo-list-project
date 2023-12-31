# Generated by Django 4.2.3 on 2023-09-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=30)),
                ('task_description', models.CharField(max_length=130)),
                ('is_completed', models.BooleanField(default=False)),
                ('first_pub', models.DateTimeField()),
                ('last_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
