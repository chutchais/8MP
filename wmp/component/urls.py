from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (ModuleListView,
					ModuleDetailView,
					ComponentListView,ComponentDetailView,
					AssembledListView,AssembledDetailView)


urlpatterns = [
	# Page
	# url(r'^$',ModuleListView.as_view(),name='list'),
	# url(r'^component/$',ComponentListView.as_view(),name='part-list'),
	# url(r'^component/(?P<slug>[-\w]+)/$',ComponentDetailView.as_view(),name='part-detail'),
 #    url(r'^(?P<slug>[-\w]+)/$',ModuleDetailView.as_view(),name='detail'),

 	url(r'^module/$',ModuleListView.as_view(),name='module-list'),
	url(r'^module/(?P<slug>[-\w]+)/$',ModuleDetailView.as_view(),name='module-detail'),
	url(r'^assembled/$',AssembledListView.as_view(),name='assembled-list'),
	url(r'^assembled/(?P<slug>[-\w]+)/$',AssembledDetailView.as_view(),name='assembled-detail'),
	
 	url(r'^$',ComponentListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',ComponentDetailView.as_view(),name='detail'),
	
    
]