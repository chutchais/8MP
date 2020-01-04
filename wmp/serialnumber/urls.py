from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import (SerialNumberDetailView,
					SerialNumberListView)


urlpatterns = [
	# Page
	url(r'^$',SerialNumberListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',SerialNumberDetailView.as_view(),name='detail'),
]