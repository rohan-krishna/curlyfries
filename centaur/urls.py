from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'centaur'

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^create/$', views.create, name='create'),
	url(r'^create/savenewstory/$', views.savenewstory, name='savenewstory'),
	url(r'^create/updatestory/$', views.updatestory, name='updatestory'),
	url(r'^show/(?P<story_id>[0-9]+)/$', views.show, name='show'),
	url(r'^delete/(?P<story_id>[0-9]+)/$', views.delete, name='delete'),
	url(r'^logout/$', auth_views.logout, name='logout'),
]