from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    NameTeam = models.CharField(max_length = 100)
    NameStaff = models.CharField(max_length = 100)
    ControlID = models.CharField(max_length = 100)
    AssociatePosition = models.CharField(max_length = 100)

def __str__(self):
    return self.title
