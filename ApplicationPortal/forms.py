from django import forms
from django.contrib.auth.models import Group
from django.forms.widgets import CheckboxSelectMultiple
from django.utils import html
from django.forms.util import ValidationError
from portal.models import *

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

"""
class Preferenceform(forms.Form):
    preference1=forms.ModelChoiceField(queryset=Event.objects.all()) #from models they shd send the name of the event alone
    preference2=forms.ModelChoiceField(queryset=Event.objects.all()) 
    preference3=forms.ModelChoiceField(queryset=Event.objects.all()) 
"""

class RegistrationForm(forms.Form):
    name=forms.CharField(help_text='Enter your first name eg. Chetan')
    rollnumber=forms.CharField(max_length = 8, help_text='Enter your Roll no eg. MM11B001')
    username=forms.RegexField(regex=r'^\w+$',max_length = 30, help_text='Your username must contain only alphabets / integers')
    password=forms.CharField(widget=forms.PasswordInput, help_text='Your password must contain at least 6 characters',min_length=6)
    confirm_password=forms.CharField(widget=forms.PasswordInput, help_text='Enter the same password')
    cgpa=forms.DecimalField(max_digits=4,decimal_places=2, help_text='eg. 8.56, 9.00, but not 7.333')
    room_number=forms.IntegerField(help_text='Room number eg. 123')
    email=forms.EmailField(help_text='email id')
    hostel=forms.CharField(help_text='hostel eg. Jamuna',max_length=20)
    phoneno=forms.IntegerField(help_text='your contact no')
    
    def clean_username(self):
    	
    	try:
    		user = User.objects.get(username = self.cleaned_data['username'])
    	except User.DoesNotExist:
    		return self.cleaned_data['username']
    	raise forms.ValidationError(u'Username already exists')
    	
    	
    	
    def clean_confirm_password(self):
    	data = self.cleaned_data
    	pass1 = data['password']
    	pass2 = data['confirm_password']
    	if pass1 and pass2:
    		if pass1 != pass2:
    			raise forms.ValidationError(u'Passwords must match')
    	return self.cleanned_data['confirm_password']

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

