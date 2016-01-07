# coding: utf-8
from .models import Book, Person, Record
from .forms import UserRegistrationForm, UserLoginForm
from django.shortcuts import render
import django.contrib.sessions
from django.shortcuts import render, redirect
from django.contrib import messages
import logging

logger = logging.getLogger('test1')
# Create your views here.

def mainPage(request):
    	return render(request, 'index.html', {})

def userLogin(request):
	logger.info(unicode(request).replace('\n' , '\t'))
	try:
		if request.method != 'POST':
			return render(request, 'login.html', {})
		name = request.POST['name']
		passwd = request.POST['passwd']
		tmpU = Person.getByName(name)
		tmpU.matchPasswd(passwd)

		#success
		logger.info(unicode(request).replace('\n', '\t') + "nico")

	except Exception as e:
		logger.error(unicode(e).replace('\n', '\t') + "niconiconi")

def userRegister(request):
	logger.info(unicode(request).replace('\n', '\t'))
	try:
		if request.method != 'POST':
			return render(request, 'register.html', {})
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			passwd1 = form.cleaned_data['passwd1']
			passwd2 = form.cleaned_data['passwd2']
			if passwd1 != passwd2:
				raise Exception(u'password do not match')
			
			user = Person.addUser(name, passwd1)
			logger.info("niconiconi")
		else:
			raise Exception(u'Invalid informations')
	except Exception as e:
		logger.error(unicode(e).replace('\n', '\t') + "nico")
		return render(request, 'register.html', {})

