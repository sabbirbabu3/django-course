from django.db import models
from music.models import Musician
# Create your models here.
class AlbumModel(models.Model):
    album_name=models.CharField(max_length=50)
    musican=models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date=models.DateField(auto_now_add=True)
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self) -> str:
        return self.album_name