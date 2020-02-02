from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from routing.models import (Routing,RoutingDetail,
								RoutingDetailNext,RoutingDetailReject,RoutingDetailAccept,
								RoutingDetailHook,RoutingDetailParameterSet)
from routing.api.serializers import (RoutingSerializer,RoutingDetailSerializer,
								RoutingNextSetSerializer,RoutingDetailNextSerializer,
								RoutingDetailAcceptSerializer,RoutingDetailAcceptSetSerializer,
								RoutingDetailRejectSerializer,RoutingDetailRejectSetSerializer,
								RoutingDetailParameterSetSerializer,
								RoutingDetailHookSerializer)

from parameter.models import Parameter
from parameter.api.serializers import ParameterSerializer


from assembly.models import Assembly_Usage
from assembly.api.serializers import AssemblyUsageSerializer


class RoutingViewSet(viewsets.ModelViewSet):
	queryset = Routing.objects.all()
	serializer_class = RoutingSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','category1','category2', 'description','status')
	filter_fields = ('name','title','category1','category2', 'description','status')

	# @detail_route(url_name='routing_detail', url_path='details/(?P<chapter_id>[0-9]+)')
	# @detail_route(url_path='details/(?P<operation_id>[/w]+)')
	# @detail_route(url_path='details/(?P<chapter_id>[0-9]+)')
	@detail_route()
	def details(self, request, pk=None):
		routing = self.get_object()
		# print (routing)
		serializer = RoutingDetailSerializer(routing.details.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)
	
	@detail_route(url_path='(?P<operation>[\w]+)')
	def get_operation(self, request, pk=None,operation=None):
		routing = self.get_object()
		serializer = RoutingDetailSerializer(
						RoutingDetail.objects.filter(routing = routing ,operation=operation
						), 
					context={'request': request}, many=True)
		return Response(serializer.data)

class RoutingDetailViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetail.objects.all()
	serializer_class = RoutingDetailSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('operation','status','routing')
	filter_fields = ('operation','status','routing')
	ordering_fields = ('ordered')

	@detail_route()
	def nexts(self, request, pk=None):
		routingdetail = self.get_object()
		# serializer = RoutingNextSetSerializer(routingdetail.nexts.all(), 
		# 			context={'request': request}, many=True)
		serializer = RoutingNextSetSerializer(routingdetail.nexts.filter(status='A'), 
					context={'request': request}, many=True)
		return Response(serializer.data)

	@detail_route()
	def accepts(self, request, pk=None):
		routingdetail = self.get_object()
		serializer = RoutingDetailAcceptSetSerializer(routingdetail.accepts.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)
	
	@detail_route()
	def rejects(self, request, pk=None):
		routingdetail = self.get_object()
		serializer = RoutingDetailRejectSetSerializer(routingdetail.rejects.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)
	
	@detail_route()
	def parameters(self, request, pk=None):
		routingdetail = self.get_object()
		serializer = RoutingDetailParameterSetSerializer(routingdetail.parameters.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)
	
	@detail_route()
	def hooks(self, request, pk=None):
		routingdetail = self.get_object()
		serializer = RoutingDetailHookSerializer(routingdetail.hooks.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)

	@detail_route()
	def assemblys(self, request, pk=None):
		routingdetail = self.get_object()
		serializer = AssemblyUsageSerializer(routingdetail.assembly_usages.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)


class RoutingDetailNextViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailNext.objects.all()
	serializer_class = RoutingDetailNextSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','status')
	filter_fields = ('name','title','status')

class RoutingDetailAcceptViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailAccept.objects.all()
	serializer_class = RoutingDetailAcceptSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','status')
	filter_fields = ('name','title','status')

class RoutingDetailRejectViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailReject.objects.all()
	serializer_class = RoutingDetailRejectSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','status')
	filter_fields = ('name','title','status')

class RoutingDetailHookViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailHook.objects.all()
	serializer_class = RoutingDetailHookSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','status')
	filter_fields = ('name','title','status')


class RoutingDetailParameterViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailParameterSet.objects.all()
	serializer_class = RoutingDetailParameterSetSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('title','status')
	filter_fields = ('title','status')

class RoutingDetailAssemblyUsageViewSet(viewsets.ModelViewSet):
	queryset = Assembly_Usage.objects.all()
	serializer_class = AssemblyUsageSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('title','status')
	filter_fields = ('title','status')