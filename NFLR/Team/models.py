from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    NameTeam = models.CharField(max_length = 100)
    Venue = models.CharField(max_length = 100)
    OwnerName = models.CharField(max_length = 100)

def __str__(self):
    return self.title
