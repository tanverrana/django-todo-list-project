# Generated by Django 4.2.3 on 2023-09-04 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskstoremodel',
            name='first_pub',
        ),
        migrations.RemoveField(
            model_name='taskstoremodel',
            name='last_pub',
        ),
    ]
