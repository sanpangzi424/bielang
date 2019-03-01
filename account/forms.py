#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('password do not match!')
        return data['password2']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

