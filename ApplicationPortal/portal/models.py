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
        
class Credentials(models.Model):
    """
    Credentials for a user 
    """
    content=models.Charfield(max_length=25)

    owner=models.ForeignKey(User)

    
    

class References(models.Model):
    """
    References for a user 
    """
    content=models.Charfield(max_length=25)

    owner=models.ForeignKey(User)

    
    

class Choice(models.Model):
    """   
    Each user has three choice.A choice corresponds to a user-event pair
    """
    choice_event=models.ForeignKey(Event)

    choice_user=models.ForeignKey(User)

    
    

class Answers(models.Model):
    """
    Each answer represents a response by a user to a question
    """
    answer_user=models.ForeignKey(User)
    answer_question=models.ForeignKey(User)
    answer_text=models.CharField(max_length=255)
    
class Userprofile(models.Model):
    """
    Userprofile
    """
    owner=models.ForeignKey(User)
    rollno=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=20)
    roomnumber=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    hostel=models.CharField(max_length=20)
