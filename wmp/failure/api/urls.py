from django.conf.urls import url
from django.contrib import admin

from .views import (
    FailureListAPIView,
    FailureDetailAPIView,
    FailureCreateAPIView,
    FailureDeleteAPIView,
    FailureUpdateAPIView
    )

urlpatterns = [
	url(r'^$', FailureListAPIView.as_view(), name='list'),
	url(r'^create/$', FailureCreateAPIView.as_view(),name='create'),
	url(r'^(?P<pk>[\w-]+)/$', FailureDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<pk>[\w-]+)/delete/$', FailureDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<pk>[\w-]+)/update/$', FailureUpdateAPIView.as_view(),name='update'),
 
]