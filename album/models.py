from typing import Any
from django.db import models
from musician.models import Musician_Model
import datetime

class Album_Model(models.Model):
    album_name = models.ForeignKey(Musician_Model, on_delete=models.CASCADE)
    album_release_date = models.DateField(default=datetime.date.today)

    
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='1')
    def __str__(self):
        return f"{self.album_name}"
   
