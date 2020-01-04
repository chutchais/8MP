# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     ItemListAPIView,
#     ItemDetailAPIView,
#     ItemCreateAPIView,
#     ItemDeleteAPIView,
#     ItemUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', ItemListAPIView.as_view(), name='list'),
# 	url(r'^create/$',ItemCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$',ItemDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', ItemDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', ItemUpdateAPIView.as_view(),name='update'),
 
# ]