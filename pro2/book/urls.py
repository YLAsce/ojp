from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.mainPage, name='home'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^register/$', views.userRegister, name='register'),
]
