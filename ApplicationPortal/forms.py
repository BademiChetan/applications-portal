from django import forms
from django.forms.widgets import CheckboxSelectMultiple()
from applications-portal.ApplicationPortal.portal.models import Events

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Preferenceform(forms.Form):
    preference1=forms.ModelChoiceField(queryset=Events.objects.all()) #from models they shd send the name of the event alone
    preference2=forms.ModelChoiceField(queryset=Events.objects.all()) 
    preference3=forms.ModelChoiceField(queryset=Events.objects.all()) 

class Registrationform(forms.Form):
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
    
