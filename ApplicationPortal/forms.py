from django import forms
from django.contrib.auth.models import Group
from django.forms.widgets import CheckboxSelectMultiple
from portal.models import *
from django.utils import html

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

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

