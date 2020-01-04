# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     PerformingListAPIView,
#     PerformingDetailAPIView,
#     PerformingCreateAPIView,
#     PerformingDeleteAPIView,
#     PerformingUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', PerformingListAPIView.as_view(), name='list'),
# 	url(r'^create/$', PerformingCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<pk>[\w-]+)/$', PerformingDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<pk>[\w-]+)/delete/$', PerformingDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<pk>[\w-]+)/update/$', PerformingUpdateAPIView.as_view(),name='update'),
 
# ]