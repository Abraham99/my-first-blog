from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    NameStadium = models.CharField(max_length = 100)
    Capacity = models.CharField(max_length = 100)
    BoxSize = models.CharField(max_length = 100)
def __str__(self):
    return self.title
