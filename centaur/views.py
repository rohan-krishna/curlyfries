# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect

from django.core import serializers

from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Story

# Create your views here.
def home(request):
	stories = Story.objects.all();
	return render(request, 'centaur/home.html', { 'stories' : stories })
# Just show the index

def index(request):
	return render(request, 'centaur/index.html', {})

# Create A New Story Page
def create(request):
	return render(request, 'centaur/index.html', {})

# Show Story
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
	me = User.objects.get(username='rohan')
	story = Story.objects.create(author=me, title=request.POST['title'])

	return JsonResponse({'message' : 'Success','story' : story.id })

@csrf_protect
def updatestory(request):
	story = Story.objects.get(pk=request.POST["story"])
	story.body = request.POST["body"]
	story.save()

	return JsonResponse({ 'message' : "Success" })