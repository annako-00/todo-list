# Generated by Django 4.2.7 on 2024-04-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_alter_project_projectid_alter_todo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
