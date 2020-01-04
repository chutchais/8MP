# from django.conf.urls import url
# from django.contrib import admin

# from .views import (
#     SymptomCodeListAPIView,
#     SymptomCodeDetailAPIView,
#     SymptomCodeCreateAPIView,
#     SymptomCodeDeleteAPIView,
#     SymptomCodeUpdateAPIView
#     )

# urlpatterns = [
# 	url(r'^$', SymptomCodeListAPIView.as_view(), name='list'),
# 	url(r'^create/$', SymptomCodeCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$', SymptomCodeDetailAPIView.as_view(), name='detail'),
# 	url(r'^(?P<slug>[\w-]+)/delete/$', SymptomCodeDeleteAPIView.as_view(),name='delete'),
# 	url(r'^(?P<slug>[\w-]+)/update/$', SymptomCodeUpdateAPIView.as_view(),name='update'),
 
# ]