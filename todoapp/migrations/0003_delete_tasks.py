# Generated by Django 5.0.7 on 2024-08-08 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_task_tasks_title_remove_tasks_dedline_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
