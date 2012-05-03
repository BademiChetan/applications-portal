from django import forms

class Loginform(forms.Forms)
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)
