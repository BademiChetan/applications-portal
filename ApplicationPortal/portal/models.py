from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class Event(models.Model)
    """
    Creates an event for a specific Type
    """
    name=models.CharField
    event_type=models.ForeignKey(Type)
    group
    
   
    
class Type(models.Model)
    """
    Creates an Event Type
    """
    name=models.CharField
    
class Question(models.Model)
    """
    Creates a question for an event
    """
    text=models.CharField
    event=models.ManyToManyField(Event)

class Update(models.Model)
    """
    Creates an object to post an update
    """
