from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from component.models import Module,Component,Assembled
from component.api.serializers import ModuleSerializer,ComponentSerializer,AssembledSerializer


class ModuleViewSet(viewsets.ModelViewSet):
	queryset = Module.objects.all()
	serializer_class = ModuleSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('number','title','category1','category2', 'description','status')
	filter_fields = ('number','title','category1','category2', 'description','status')
	lookup_field = 'number'

class ComponentViewSet(viewsets.ModelViewSet):
	queryset = Component.objects.all()
	serializer_class = ComponentSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('number','title','category1','category2', 'description','status')
	filter_fields = ('number','title','category1','category2', 'description','status')
	lookup_field = 'pk'


class AssembledViewSet(viewsets.ModelViewSet):
	queryset = Assembled.objects.all()
	serializer_class = AssembledSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('number__number','refdes','pn')
	filter_fields = ('number__number','refdes','pn')
	lookup_field = 'slug'