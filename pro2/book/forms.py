# coding: utf-8
from django import forms
from .const import Const

class UserRegistrationForm(forms.Form):
	name = forms.CharField(max_length = Const.AUTHOR_NAME_MAX_LENGTH)
	passwd1 = forms.CharField(max_length = Const.PASSWD_MAX_LENGTH)
	passwd2 = forms.CharField(max_length = Const.PASSWD_MAX_LENGTH)

class UserLoginForm(forms.Form):
	name = forms.CharField(max_length = Const.AUTHOR_NAME_MAX_LENGTH)
	passwd = forms.CharField(max_length = Const.PASSWD_MAX_LENGTH)

