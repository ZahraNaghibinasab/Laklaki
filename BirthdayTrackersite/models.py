from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Events(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    event = models.TextField()


class Birth(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    event = models.TextField()


class Death(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    event = models.TextField()

class Months(models.Model):
    month = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    rock = models.CharField(max_length=50)
    chanceDay = models.CharField(max_length=50)
    planet = models.CharField(max_length=50)


class Whole(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    event = models.TextField()
    birth = models.TextField()
    death = models.TextField()