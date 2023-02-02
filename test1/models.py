from django.db import models


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description
