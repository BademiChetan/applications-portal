from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class Event(models.Model)
    """
    Creates an event for a specific Type
    """
    name=models.CharField
    group=models.ForeignKey(Group)
    
    def __unicode__(self):
        return self.name
                
    class Meta:
        ordering = ['name']
        
class Question(models.Model)
    """
    Creates a question for an event
    """
    question=models.CharField
    event=models.ManyToManyField(Event)
    
    def __unicode__(self):
        return self.name

class Update(models.Model)
    """
    Creates an object to post an update
    """
    update_text=models.CharField
    timestamp=models.DateTimeField