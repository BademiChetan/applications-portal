from django.db import models
from django.contrib.auth.models import *
import datetime

# Create your models here.

class Event(models.Model):
    """
    Creates an event for a specific Type
    """
    name=models.CharField(_('Event'), max_length=255, unique=True)
    group=models.ForeignKey(Group)
    
    def __unicode__(self):
        return self.name
                
    class Meta:
        ordering = ['name']
        
class Question(models.Model):
    """
    Creates a question for an event
    """
    question=models.CharField(_('Question'), max_length=255)
    event=models.ManyToManyField(Event)
    
    def __unicode__(self):
        return self.question

class Update(models.Model):
    """
    Creates an object to post an update
    """
    update_text=models.CharField(_('Update'), max_length=255)
    timestamp=models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.update_text
        
class Credentials(models.Model):
    """
    Credentials for a user 
    """
    content=models.CharField(_('Credentials'), max_length=255)
    user=models.ForeignKey(User)
    
    def __unicode__(self):
        return self.content
    
class References(models.Model):
    """
    References for a user 
    """
    content=models.CharField(_('References'), max_length=255)
    user=models.ForeignKey(User)
    
    def __unicode__(self):
        return self.content
    
class Choice(models.Model): #modifications required
    """   
    Each user has three choices.
    """
    choice1=choice2=choice3=models.ForeignKey(Event)
    user=models.ForeignKey(User)
    
    def __unicode__(self):
        return self.user
    
class Answers(models.Model):
    """
    Each answer represents a response by a user to a question
    """
    user=models.ForeignKey(User)
    question=models.ForeignKey(Question)
    answer=models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.answer
    
class UserProfile(User, models.Model):
    """
    Userprofile
    """
    ph_no=models.BigIntegerField()
    is_core=models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.username
    
