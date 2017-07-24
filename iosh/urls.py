from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'iosh'

urlpatterns=[
	url(r'^$', views.index, name='index')
]