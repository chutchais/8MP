from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (ComponentListView,
					ComponentDetailView)


urlpatterns = [
	# Page
	url(r'^$',ComponentListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',ComponentDetailView.as_view(),name='detail'),
]