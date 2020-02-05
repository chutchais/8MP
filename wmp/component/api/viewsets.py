from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from component.models import Component,Part
from component.api.serializers import ComponentSerializer,PartSerializer


class ComponentViewSet(viewsets.ModelViewSet):
	queryset = Component.objects.all()
	serializer_class = ComponentSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('number','title','category1','category2', 'description','status')
	filter_fields = ('number','title','category1','category2', 'description','status')
	lookup_field = 'slug'

class PartViewSet(viewsets.ModelViewSet):
	queryset = Part.objects.all()
	serializer_class = PartSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('number','title','category1','category2', 'description','status')
	filter_fields = ('number','title','category1','category2', 'description','status')
	lookup_field = 'slug'