from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    NameTeam = models.CharField(max_length = 100)
    NamePlayer = models.CharField(max_length = 100)
    NoPlayer = models.CharField(max_length = 100)
    PlayerPosition = models.CharField(max_length = 100)

def __str__(self):
    return self.title
