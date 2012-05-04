from django import forms
from django.contrib.auth.models import Group
from django.forms.widgets import CheckboxSelectMultiple
from portal.models import *
from django.utils import html

'''
This is to define a submit button within a form field so that each preference has a submit button.

Usage:

SubmitButtonField(label="", initial=u"Your submit button text")


class SubmitButtonWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        return '<input type="submit" name="%s" value="%s">' % (html.escape(name), html.escape(value))


class SubmitButtonField(forms.Field):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = {}
        kwargs["widget"] = SubmitButtonWidget

        super(SubmitButtonField, self).__init__(*args, **kwargs)

    def clean(self, value):
        return value
        
'''        

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Preferenceform(forms.Form):
    preference1=forms.ModelChoiceField(queryset=Event.objects.all()) #from models they shd send the name of the event alone
    preference2=forms.ModelChoiceField(queryset=Event.objects.all()) 
    preference3=forms.ModelChoiceField(queryset=Event.objects.all()) 

class RegistrationForm(forms.Form):
    name=forms.CharField()
    rollnumber=forms.CharField()
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
<<<<<<< HEAD
    cgpa=forms.IntegerField()
    room number=forms.IntergerField()
    email=EmailField()



class AddGroup(form.ModelForm):
    class Meta:
        model = Group
   	widgets={'permissions':forms.MultipleChoiceField(widget=CheckboxSelectMultiple())}
=======
    cgpa=forms.DecimalField(max_digits=4,decimal_places=2)
    room_number=forms.IntegerField()
    email=forms.EmailField()
    hostel=forms.CharField()
    phoneno=forms.IntegerField()
>>>>>>> f7b78146c03ce585222c610db06513189dfd2dd8

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
        fields={'user', 'rollno', 'room_number', 'hostel', 'ph_no', 'is_core','cgpa',}     
        widgets={'user':forms.HiddenInput(),}  

