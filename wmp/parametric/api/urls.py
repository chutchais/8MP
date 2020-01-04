# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#    ParametricListAPIView,
#     ParametricDetailAPIView,
#     ParametricCreateAPIView,
#     ParametricDeleteAPIView,
#     ParametricUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', ParametricListAPIView.as_view(), name='list'),
# 	url(r'^create/$', ParametricCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<pk>[\w-]+)/$', ParametricDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<pk>[\w-]+)/delete/$', ParametricDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<pk>[\w-]+)/update/$', ParametricUpdateAPIView.as_view(),name='update'),
 
# ]