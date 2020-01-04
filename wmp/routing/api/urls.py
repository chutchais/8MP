# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     RoutingListAPIView,
#     RoutingDetailAPIView,
#     RoutingCreateAPIView,
#     RoutingDeleteAPIView,
#     RoutingUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', RoutingListAPIView.as_view(), name='list'),
# 	url(r'^create/$',RoutingCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$',RoutingDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\wRouting-]+)/delete/$', RoutingDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', RoutingUpdateAPIView.as_view(),name='update'),
 
# ]