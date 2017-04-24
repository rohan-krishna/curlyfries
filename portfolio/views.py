# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
	return render(request, 'portfolio/index.html', {})

def login(request):
	return render(request, 'portfolio/login.html', {})