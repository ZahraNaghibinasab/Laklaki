from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Events(models.Model):
    day = models.IntegerField()
    month =models.IntegerField()
    year = models.IntegerField()
    event = models.TextField(max_length=200)

class Birth(models.Model):
    day = models.IntegerField()
    month =models.IntegerField()
    year = models.IntegerField()
    event = models.TextField(max_length=200)

class Death(models.Model):
    day = models.IntegerField()
    month =models.IntegerField()
    year = models.IntegerField()
    event = models.TextField(max_length=200)