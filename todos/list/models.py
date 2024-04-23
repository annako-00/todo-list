from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
     projectid=models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
     title=models.CharField(max_length=100)
     cdate=models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.title

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    description = models.TextField()
    status =models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.description
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.id = uuid.uuid4()
        super(Todo, self).save(*args, **kwargs)

