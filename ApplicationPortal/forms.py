from django import forms
from applications-portal.ApplicationPortal.models import Events

class Loginform(forms.Forms)
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Preferenceform(forms.Forms)
    preference1=forms.ModelChoiceField(queryset=Events.objects.all()) #from models they shd send the name of the event alone
    preference2=forms.ModelChoiceField(queryset=Events.objects.all()) 
    preference3=forms.ModelChoiceField(queryset=Events.objects.all()) 
