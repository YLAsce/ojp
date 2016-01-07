# -*- coding:utf-8 -*-

from django.db import models
from hashlib import sha1, sha256
from .const import Const

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length = Const.BOOK_NAME_MAX_LENGTH)
	author = models.CharField(max_length = Const.AUTHOR_NAME_MAX_LENGTH)
	isbn = models.CharField(max_length = Const.ISBN_MAX_LENGTH)
	press = models.CharField(max_length = Const.PRESS_NAME_MAX_LENGTH)
	num_avaliable = models.PositiveIntegerField(default = 1)
	num_total = models.PositiveIntegerField(default = 1) 
	pic = models.ImageField(default = 'None/no-img.jpg')
	
	def __unicode__(self):
		return self.isbn

class Person(models.Model):
	name = models.CharField(max_length = Const.AUTHOR_NAME_MAX_LENGTH)
	passwd = models.CharField(max_length = Const.PASSWD_MAX_LENGTH)
	
	def __unicode__(self):
		return self.name

	def matchPasswd(self,passwd):
		tmppasswd = sha1(str(passwd)).hexdigest()
		tmppasswd = sha256(tmppasswd + Const.PASSWD_SALT).hexdigest()
		if(tmppasswd == self.passwd):
			return True
		else:
			raise Exception(u'Password does not match')
	
	def _encodePasswd(self):
		tmppasswd = sha1(str(self.passwd)).hexdigest()
		tmppasswd = sha256(tmppasswd + Const.PASSWD_SALT).hexdigest()
		self.passwd = tmppasswd
	
	def _checkInfo(self):
		if len(self.name) < Const.AUTHOR_NAME_MIN_LENGTH or len(self.name) > Const.AUTHOR_NAME_MAX_LENGTH:
			raise Exception(u'name length is unavaliable!')

		for ch in self.name:
			if ch == ' ':
				raise Exception(u'name must not contain spaces')

		flag = True
		try:
			t = Person.getByName(self.name)
			flag = False
		except:
			pass
		
		if not flag:
			raise Exception(u'name has been used!')

		if len(self.passwd) < Const.PASSWD_MIN_LENGTH or len(self.passwd) > Const.PASSWD_MAX_LENGTH:
			raise Exception(u'password length is unavaliable')

		return True

	@classmethod
	def getByName(cls, request_name):
		return cls.objects.get(name = request_name)
	
	@classmethod
	def addUser(cls, name, passwd):
		try:
			p = Person()
			p.name = name
			p.passwd = passwd
			p._checkInfo()
			p._encodePasswd()
			p.save()
			return p
		except Exception as e:
			raise e

class Record(models.Model):
	in_or_out = models.BooleanField()
	date = models.DateTimeField()
	person_name = models.CharField(max_length = Const.AUTHOR_NAME_MAX_LENGTH)
	book_name = models.CharField(max_length = Const.BOOK_NAME_MAX_LENGTH)	
	book_isbn = models.CharField(max_length = Const.ISBN_MAX_LENGTH)
	
	def __unicode__(self):
		return self.person_name + self.book_isbn
