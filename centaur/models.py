# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Story(models.Model):
	"""docstring for Story"""
	author = models.ForeignKey('auth.User')
	title = models.CharField( max_length = 200, blank = True )
	body = models.TextField( blank = True, null = True)
	created_at = models.DateTimeField( default = timezone.now )
	updated_at = models.DateTimeField( default = timezone.now )

	class Meta:
		verbose_name='Story'
		verbose_name_plural = 'Stories'
	
	def __str__(self):
		return self.title
		