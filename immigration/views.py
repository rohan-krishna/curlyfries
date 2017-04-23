# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
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
		return render(request, 'immigration/auth/login.html',{ 'next_url' : request.GET['next'] })
	else:
		return HttpResponseRedirect(reverse('immigration:index'))

def post_login(request):
	username = request.POST['username']
	password = request.POST['password']
	next_url = request.POST['next_url']

	user = authenticate(username=username, password=password)

	if user is not None:
		djangoLogin(request, user)
		return redirect(next_url)
	else:
		return HttpResponseRedirect(reverse('immigration:index'))


def logout(request):
	djangoLogout(request)
	return HttpResponseRedirect(reverse('immigration:index'))