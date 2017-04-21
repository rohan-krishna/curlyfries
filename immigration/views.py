# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as djangoLogin
from django.contrib.auth import logout as djangoLogout

# Create your views here.
def index(request):
	# Check for Passport & Valid Documents
	# If No Visa is stamped, take em to camp .. sorry I mean detain and Interrogate
	if request.user.is_authenticated:
		return render(request, "household/index.html", {})
	else:
		return HttpResponseRedirect(reverse('immigration:login'))

def login(request):
	if not request.user.is_authenticated:
		return render(request, 'immigration/auth/login.html',{})
	else:
		return HttpResponseRedirect(reverse('immigration:index'))

def post_login(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user is not None:
		djangoLogin(request, user)
		return HttpResponseRedirect(reverse('immigration:index'))
	else:
		return HttpResponseRedirect(reverse('immigration:index'))


def logout(request):
	djangoLogout(request)
	return HttpResponseRedirect(reverse('immigration:index'))