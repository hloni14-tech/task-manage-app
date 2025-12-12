from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=2990)
    desription = models.TextField()
    due_date = models.DateTimeField(auto_now=add)
    prority = models.Choices[
        "H": "High",
        "M": "Medium",
        "L": "Low",
    ]
    
class StatusModel(models.Model):
    status = models.Choices[
        "P": "Pending",
        "C": "Completed",
    ]

class TaskStatusModel(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusModel, on_delete=models.CASCADE)

class CommntModel(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    comment = models.TextField()