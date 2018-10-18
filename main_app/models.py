from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.forms import TextInput

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('collections_detail', kwargs={'collection_id': self.id})
    

class Poet(models.Model):
    name = models.CharField(max_length=100)
    born = models.CharField('Birth Date', max_length=100, help_text='Month Day, Year')
    died = models.CharField('Death Date', max_length=100, blank=True)
    biography = models.TextField(max_length=1000)
    period = models.CharField('Period(s)', max_length=100)
    
    def __str__(self):
        return self.name

class Poem(models.Model):
    name = models.CharField(max_length=100)
    poemcontent = models.TextField('Poem', max_length=5000)
    date = models.CharField('Written', max_length=100)
    source = models.CharField(max_length=500)
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)
    collection = models.ManyToManyField(Collection)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Comment(models.Model):
    content = models.TextField('COMMENT', max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)

    def __str__(self):
        return f'Commment: {self.content}'

        # widget=TextInput(attrs={'placeholder':'Month Day, Year'})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

class CoverPhoto(models.Model):
    url = models.CharField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.url