# from django.conf.urls import url
# from django.contrib import admin
# from rest_framework.urlpatterns import format_suffix_patterns

# from .views import (
#     # SnippetListAPIView,
#     # SnippetDetailAPIView,
#     # SnippetCreateAPIView,
#     # SnippetDeleteAPIView,
#     # SnippetUpdateAPIView,
#     SnippetList,
#     SnippetDetail
#     )

# urlpatterns = [
# 	url(r'^$', SnippetList.as_view(), name='list'),
# 	# url(r'^create/$',SnippetCreateAPIView.as_view(),name='create'),
# 	url(r'^(?P<slug>[\w-]+)/$',SnippetDetail.as_view(), name='detail'),
# 	# url(r'^(?P<slug>[\w-]+)/delete/$', SnippetDeleteAPIView.as_view(),name='delete'),
# 	# url(r'^(?P<slug>[\w-]+)/update/$', SnippetUpdateAPIView.as_view(),name='update'),
 
# ]


# urlpatterns = format_suffix_patterns(urlpatterns)