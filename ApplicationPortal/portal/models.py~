from django.db import models
from django.contrib.auth.models import *
import datetime

# Create your models here.

class Event(models.Model):
    """
    Creates an event for a specific Type
    """
    name=models.CharField(_('Event'), max_length=200, unique=True)
    group=models.ForeignKey(Group)
    
    def __unicode__(self):
        return self.name
                
    class Meta:
        ordering = ['name']
        
class Question(models.Model):
    """
    Creates a question for an event
    """
    question=models.CharField(_('Question'), max_length=200)
    event=models.ManyToManyField(Event)
    
    def __unicode__(self):
        return self.question

class Update(models.Model):
    """
    Creates an object to post an update
    """
    update_text=models.CharField(_('Update'), max_length=200)
    timestamp=models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.update_text

