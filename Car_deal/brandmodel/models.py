from django.db import models

class BarndModel(models.Model):
    brand = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.brand  # Corrected to access the 'brand' attribut
    
    def car_count(self):
        return self.carmodel_set.count()