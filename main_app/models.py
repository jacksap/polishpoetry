from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Poet(models.Model):
    name = models.CharField(max_length=100)
    born = models.DateField('Birth Date')
    died = models.DateField('Death Date')
    biography = models.TextField(max_length=500)
    period = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Poem(models.Model):
    name = models.CharField(max_length=100)
    poemcontent = models.TextField(max_length=5000)
    date = models.DateField('Date Written')
    source = models.CharField(max_length=500)
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
