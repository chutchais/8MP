from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (AssemblyDetailView,
					AssemblyListView)


urlpatterns = [
	# Page
	url(r'^$',AssemblyListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',AssemblyDetailView.as_view(),name='detail'),
]