from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm, Textarea

class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField()
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
