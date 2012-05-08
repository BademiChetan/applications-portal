from django import forms
from django.contrib.auth.models import Group
from django.forms.widgets import CheckboxSelectMultiple
from portal.models import *
from django.utils import html

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class Preferenceform(forms.Form):
    preference1=forms.ModelChoiceField(queryset=Event.objects.all(),empty_label="Select") #from models they shd send the name of the event alone
    preference2=forms.ModelChoiceField(queryset=Event.objects.all(),empty_label="Select") 
    preference3=forms.ModelChoiceField(queryset=Event.objects.all(),empty_label="Select") 


class RegistrationForm(forms.Form):
    name=forms.CharField()
    rollnumber=forms.CharField()
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    cgpa=forms.IntegerField()
    room_number=forms.IntegerField()
    email=forms.EmailField()
    hostel=forms.CharField()
    phoneno=forms.IntegerField()

"""
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = {'question': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        exclude = {'timestamp'}
        widgets = {'update': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class CredentialsForm(forms.ModelForm):
    class Meta:
        model = Credentials
        exclude = {'user'}
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        exclude = {'user'}
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = {'user'}
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = {'answer'}
        widgets = {'answer': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
"""

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = {'is_core'}

class AddGroup(forms.ModelForm):
    class Meta:
        model = Group
 
class AddCore(forms.Form):
    name=forms.CharField()
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
  
class CoreUserProfile(forms.ModelForm):
    class Meta:
        model=UserProfile 
        fields={'user', 'rollno', 'room_number', 'hostel', 'ph_no', 'is_core', 'cgpa',}     
        widgets={'user':forms.HiddenInput(), 'is_core':forms.HiddenInput(),}  

