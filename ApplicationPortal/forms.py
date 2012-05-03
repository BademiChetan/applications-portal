from django import forms
from applications-portal.ApplicationPortal.portal.models import Events

class Loginform(forms.Forms)
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Preferenceform(forms.Forms)
    preference1=forms.ModelChoiceField(queryset=Events.objects.all()) #from models they shd send the name of the event alone
    preference2=forms.ModelChoiceField(queryset=Events.objects.all()) 
    preference3=forms.ModelChoiceField(queryset=Events.objects.all()) 

class Registrationform(froms.Forms)
    name=forms.CharField()
    rollnumber=forms.CharField()
    username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    cgpa=forms.IntegerField()
    room_number=forms.IntergerField()
    email=forms.EmailField()
    hostel=forms.Charfield()
