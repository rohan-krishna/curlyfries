# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect

from django.core import serializers

from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Story

# Create your views here.
@login_required(login_url = 'immigration:login')
def home(request):
	me = request.user
	stories = Story.objects.filter( author=me ).order_by('-updated_at');
	return render(request, 'centaur/home.html', { 'stories' : stories })
# Just show the index

@login_required(login_url = 'immigration:login')
def index(request):
	return render(request, 'centaur/index.html', {})

# Create A New Story Page
@login_required(login_url = 'immigration:login')
def create(request):
	return render(request, 'centaur/index.html', {})

# Show Story
@login_required(login_url = 'immigration:login')
def show(request,story_id):
	story = get_object_or_404(Story, pk=story_id)
	context = { "story" : story }
	return render(request, 'centaur/show.html', context)

# Delete A Story
def delete(request, story_id):
	story = get_object_or_404(Story, pk=story_id)
	story.delete()
	return HttpResponseRedirect(reverse('centaur:home'))

# Create a new story when the first keystroke is touched
# on title input field
@csrf_protect
def savenewstory(request):
	me = request.user
	story = Story.objects.create(author=me, title=request.POST['title'])

	return JsonResponse({'message' : 'Success','story' : story.id })

@csrf_protect
def updatestory(request):
	story = Story.objects.get(pk=request.POST["story"])
	story.title = request.POST["title"]
	story.body = request.POST["body"]
	story.save()

	return JsonResponse({ 'message' : "Success" })