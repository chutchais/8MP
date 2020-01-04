# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     OperationListAPIView,
#     OperationDetailAPIView,
#     OperationCreateAPIView,
#     OperationDeleteAPIView,
#     OperationUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', OperationListAPIView.as_view(), name='list'),
# 	url(r'^create/$',OperationCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$',OperationDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', OperationDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', OperationUpdateAPIView.as_view(),name='update'),
 
# ]