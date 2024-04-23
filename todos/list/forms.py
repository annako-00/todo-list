from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class todoForm(forms.Form):
     title=forms.CharField()
     

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['description', 'status'] 
