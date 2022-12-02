from dataclasses import fields
from importlib.metadata import files
from django import forms
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User

class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
