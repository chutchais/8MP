# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     SerialNumberListAPIView,
#     SerialNumberDetailAPIView,
#     SerialNumberCreateAPIView,
#     SerialNumberDeleteAPIView,
#     SerialNumberUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', SerialNumberListAPIView.as_view(), name='list'),
# 	url(r'^create/$', SerialNumberCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$', SerialNumberDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', SerialNumberDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', SerialNumberUpdateAPIView.as_view(),name='update'),
 
# ]