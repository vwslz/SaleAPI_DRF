from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sale.models import Customer

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.firstname = self.cleaned_data['first_name']
        user.lasttname = self.cleaned_data['first_name']

        if commit:
            user.save()
        return user