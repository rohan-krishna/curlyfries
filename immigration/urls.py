# Immigration is responsible for Authentication & Authorization in our App
# 
from django.conf.urls import url
from . import views

app_name = 'immigration'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^post_login/$', views.post_login, name='post_login'),
	url(r'^logout/$', views.logout, name='logout'),
]