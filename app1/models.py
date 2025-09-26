from django.db import models

# Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     roll = models.IntegerField()
#     age = models.IntegerField()
#     message = models.TextField()
#     email = models.EmailField()
#     YesNo = models.BooleanField()
#     hobby = models.CharField(blank=True)

class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return self.task
        
