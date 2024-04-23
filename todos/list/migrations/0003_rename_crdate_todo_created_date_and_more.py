# Generated by Django 4.2.7 on 2024-04-22 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_remove_todo_pid_project_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='crdate',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='todoid',
        ),
        migrations.AddField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='project',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='list.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectid',
            field=models.UUIDField(default=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
