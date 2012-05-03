from django import forms
from django.forms.widgets import CheckboxSelectMultiple()
from applications-portal.ApplicationPortal.portal.models import Events
from portal.models import *

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Preferenceform(forms.Form):

class LoginForm(forms.Forms):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class PreferenceForm(forms.Forms):

    preference1=forms.ModelChoiceField(queryset=Events.objects.all()) #from models they shd send the name of the event alone
    preference2=forms.ModelChoiceField(queryset=Events.objects.all()) 
    preference3=forms.ModelChoiceField(queryset=Events.objects.all()) 


class Registrationform(forms.Form):

class RegistrationForm(froms.Forms):

    name=forms.CharField()
    rollnumber=forms.CharField()
    username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    cgpa=forms.IntegerField()
    room_number=forms.IntergerField()
    email=forms.EmailField()
    hostel=forms.Charfield()


class Addgroup(form.Form):
    name=forms.CharField()
    permissions=forms.MultipleChoiceField(widget=CheckboxSelectMultiple())
    

    
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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = {'is_core'}
        

