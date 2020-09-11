from django.db import models

# Create your models here.

class Post(models.Model):  
    postid  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    body = models.CharField(max_length=50)
