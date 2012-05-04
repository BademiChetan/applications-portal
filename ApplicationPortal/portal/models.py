from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import *
import datetime
# Create your models here.

class UserProfile(models.Model):
    """
    Userprofile
    """    
    user=models.ForeignKey(User)
    rollno=models.CharField(max_length=20)   
    roomnumber=models.CharField(max_length=20)
    hostel=models.CharField(max_length=20)
    ph_no=models.BigIntegerField(max_length=23)    
    is_core=models.BooleanField(default=False)
    
    group=models.ForeignKey(Group)
    
    def __unicode__(self):
        return self.user
   
class Event(models.Model):
    """
    Creates an event for a specific Type
    """
    name=models.CharField(max_length=255, unique=True)
    group=models.ForeignKey(Group)
    
    def __unicode__(self):
        return self.name
                
    class Meta:
        ordering = ['name']
        
class Question(models.Model):
    """
    Creates a question for an event
    """
    question=models.CharField(max_length=255)
    event=models.ForeignKey(Event)
    
    def __unicode__(self):
        return self.question

class Update(models.Model):
    """
    Creates an object to post an update
    """
    update_text=models.CharField(max_length=255)
    timestamp=models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.update_text
        
class Credentials(models.Model):
    """
    Credentials for a user 
    """
    user=models.ForeignKey(UserProfile)
    content=models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.content

class References(models.Model):
    """
    References for a user 
    """
    user=models.ForeignKey(UserProfile)
    content=models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.content
    
class Choice(models.Model): #modifications required
    """   
    Each user has three choices.
    """
    event=models.ForeignKey(Event)
    pref_no=models.IntegerField()
    user=models.ForeignKey(UserProfile)
    is_accepted=models.IntegerField(default=0) #0-unevaluated,1-accepted,-1-rejected

    
    def __unicode__(self):
        return self.user

class Answer(models.Model):
    """
    Each answer represents a response by a user to a question
    """
    user=models.ForeignKey(UserProfile)
    question=models.ForeignKey(Question)
    answer=models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.answer
    

