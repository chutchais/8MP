# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     WorkOrderListAPIView,
#     WorkOrderDetailAPIView,
#     WorkOrderCreateAPIView,
#     WorkOrderDeleteAPIView,
#     WorkOrderUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', WorkOrderListAPIView.as_view(), name='list'),
# 	url(r'^create/$', WorkOrderCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$', WorkOrderDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', WorkOrderDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', WorkOrderUpdateAPIView.as_view(),name='update'),
 
# ]