# Generated by Django 4.2.7 on 2024-04-23 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_alter_todo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='id',
            new_name='todo_id',
        ),
    ]
