from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category_model(models.Model):
    category_name = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return self.category_name
