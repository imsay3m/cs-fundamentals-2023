# Generated by Django 5.0.1 on 2024-01-03 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='category',
            new_name='categories',
        ),
    ]
