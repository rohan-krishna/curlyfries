# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
	# Check for Passport & Valid Documents
	# If No Visa is stamped, take em to camp .. sorry I mean detain and Interrogate
	if request.user.is_authenticated:
		return HttpResponse("Curly Fries Welcomes you! Access is not Guranteed! But you'll get a chance to Apply!")
	else:
		return HttpResponseRedirect(reverse('immigration:login'))

def login(request):
	if not request.user.is_authenticated:
		return render(request, 'immigration/auth/login.html',{})
	else:
		return HttpResponseRedirect(reverse('immigration:index'))