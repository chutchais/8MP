from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (ParametricDetailView,
					ParametricListView)


urlpatterns = [
	# Page
	url(r'^$',ParametricListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',ParametricDetailView.as_view(),name='detail'),
]