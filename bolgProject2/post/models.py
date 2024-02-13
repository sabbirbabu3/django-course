from django.db import models
from cetagory.models import Cetagories
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    categories=models.ManyToManyField(Cetagories)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='post/uploads/', blank=True, null=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)# ai mail die akta comments kora jabe
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"comments By: {self.name}"
