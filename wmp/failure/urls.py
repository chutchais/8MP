from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (FailureDetailView,
					FailureListView)


urlpatterns = [
	# Page
	url(r'^$',FailureListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',FailureDetailView.as_view(),name='detail'),
]