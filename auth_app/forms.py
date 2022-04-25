from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class PersonForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta: 
        model = User
        fields = ['first_name','last_name','email','username','password']
        

        
class PersonLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','password']
