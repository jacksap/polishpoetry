from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Poet(models.Model):
    name = models.CharField(max_length=100)
    born = models.DateField('Birth Date')
    died = models.DateField('Death Date')
    biography = models.TextField(max_length=1000)
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

class Comment(models.Model):
    content = models.TextField('Comment', max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)




