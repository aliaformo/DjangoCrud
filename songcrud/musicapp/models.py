from django.db import models
from datetime import datetime
from django.conf import settings


# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=80)
    las_name = models.CharField(max_length=100)
    age = models.IntegerField()

def __str__(self):
    return self.first_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    
    
def __str__(self):
    return self.title


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    
    
    
def __str__(self):
    return self.content




