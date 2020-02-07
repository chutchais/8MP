from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (ModuleListView,
					ModuleDetailView,
					ComponentListView,ComponentDetailView)


urlpatterns = [
	# Page
	url(r'^$',ModuleListView.as_view(),name='list'),
	url(r'^component/$',ComponentListView.as_view(),name='part-list'),
	url(r'^component/(?P<slug>[-\w]+)/$',ComponentDetailView.as_view(),name='part-detail'),
    url(r'^(?P<slug>[-\w]+)/$',ModuleDetailView.as_view(),name='detail'),


    url(r'^$',ComponentListView.as_view(),name='list'),
	url(r'^module/$',ModuleListView.as_view(),name='module-list'),
	url(r'^module/(?P<slug>[-\w]+)/$',ModuleDetailView.as_view(),name='module-detail'),
    url(r'^(?P<slug>[-\w]+)/$',ComponentDetailView.as_view(),name='detail'),
]