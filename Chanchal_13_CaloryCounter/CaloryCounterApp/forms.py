from django import forms
from CaloryCounterApp.models import *
from django.contrib.auth.forms import UserCreationForm

class registerForm(UserCreationForm):
    class Meta:
        model = customUser
        fields = ['username', 'email', 'password1', 'password2']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = profileModel
        fields = '__all__'
        exclude = ['user', 'bmr']


class calorieConsumedForm(forms.ModelForm):
    class Meta:
        model = consumedColorieModel
        fields = '__all__'
        exclude = ['user']