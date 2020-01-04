from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (ProductDetailView,
					ProductListView)


urlpatterns = [
	# Page
	url(r'^$',ProductListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',ProductDetailView.as_view(),name='detail'),
]