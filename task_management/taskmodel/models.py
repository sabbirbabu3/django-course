from django.db import models
from taskCategory.models import Category_model

# Create your models here.
class Task_model(models.Model):
    task_title=models.CharField(max_length=50)
    task_discription=models.TextField()
    is_complete=models.BooleanField(default=False)
    task_asgin_date=models.DateField()
    category=models.ManyToManyField(Category_model)

    def __str__(self):
        return self.task_title