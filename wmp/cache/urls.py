from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import getcache
urlpatterns = [
	# Page
	url(r'^$',getcache,name='list'),
	# url(r'^(?P<key>[-\w]+)$',get_cache,name='cache'),
]