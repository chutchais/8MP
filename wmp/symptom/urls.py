from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (SymptomCodeDetailView,
					SymptomCodeListView)


urlpatterns = [
	# Page
	url(r'^$',SymptomCodeListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',SymptomCodeDetailView.as_view(),name='detail'),
]