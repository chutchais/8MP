from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (PerformingDetailView,
					PerformingListView)


urlpatterns = [
	# Page
	url(r'^$',PerformingListView.as_view(),name='list'),
    url(r'^(?P<uid>[-\w]+)$',PerformingDetailView.as_view(),name='detail'),
]