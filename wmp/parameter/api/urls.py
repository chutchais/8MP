# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     ParameterListAPIView,
#     ParameterDetailAPIView,
#     ParameterCreateAPIView,
#     ParameterDeleteAPIView,
#     ParameterUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', ParameterListAPIView.as_view(), name='list'),
# 	url(r'^create/$',ParameterCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$',ParameterDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', ParameterDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', ParameterUpdateAPIView.as_view(),name='update'),
 
# ]