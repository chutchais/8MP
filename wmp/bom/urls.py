from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (BomDetailView,
					BomListView)


urlpatterns = [
	# Page
	url(r'^$',BomListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',BomDetailView.as_view(),name='detail'),
]