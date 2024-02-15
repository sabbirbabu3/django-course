from django.db import models
from brandmodel.models import BarndModel
from django.contrib.auth.models import User

class CarModel(models.Model):
    image = models.ImageField(upload_to='uploads/')
    car_name = models.CharField(max_length=50)
    car_price = models.IntegerField(null=True)
    brand = models.ForeignKey(BarndModel, on_delete=models.CASCADE, verbose_name="Brand")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    details=models.TextField(blank=True)

    def __str__(self):
        return self.car_name
    
    

class comments(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name