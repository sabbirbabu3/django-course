from django.db import models

# Create your models here.
class Musician_Model(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emal=models.EmailField()
    phone_number=models.IntegerField()
    instrument_type=models.CharField(max_length=50)
   
    def __str__(self):
        return f"{self.first_name}"