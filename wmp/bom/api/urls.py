# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     BomListAPIView,
#     BomDetailAPIView,
#     BomCreateAPIView,
#     BomDeleteAPIView,
#     BomUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', BomListAPIView.as_view(), name='list'),
# 	url(r'^create/$',BomCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$',BomDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', BomDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', BomUpdateAPIView.as_view(),name='update'),
 
# ]