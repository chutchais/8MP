from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (RoutingDetailView,
					RoutingListView,
					RoutingOperationDetailView,
					RoutingDetailNextView,
					RoutingDetailAcceptView,
					RoutingDetailRejectView,
					RoutingDetailHookView)


urlpatterns = [
	# Page
	url(r'^$',RoutingListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',RoutingDetailView.as_view(),name='detail'),
    url(r'^detail/(?P<slug>[-\w]+)/$',RoutingOperationDetailView.as_view(),name='operation-detail'),
    url(r'^next/(?P<slug>[-\w]+)/$',RoutingDetailNextView.as_view(),name='next-detail'),
    url(r'^accept/(?P<slug>[-\w]+)/$',RoutingDetailAcceptView.as_view(),name='accept-detail'),
    url(r'^reject/(?P<slug>[-\w]+)/$',RoutingDetailRejectView.as_view(),name='reject-detail'),
    url(r'^hook/(?P<slug>[-\w]+)/$',RoutingDetailHookView.as_view(),name='hook-detail'),
]