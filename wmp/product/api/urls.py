# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     ProductListAPIView,
#     ProductDetailAPIView,
#     ProductCreateAPIView,
#     ProductDeleteAPIView,
#     ProductUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', ProductListAPIView.as_view(), name='list'),
# 	url(r'^create/$',ProductCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$',ProductDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', ProductDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', ProductUpdateAPIView.as_view(),name='update'),
 
# ]