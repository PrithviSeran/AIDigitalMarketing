from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Campaign

class MyForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

class PagesWanted(forms.Form):

    count = forms.IntegerField(label='How many pages do you want to visit? ')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'use', 'user_info', 'purpose', 'target_audience']

    