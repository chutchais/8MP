from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from parameter.models import Parameter
from parameter.api.serializers import ParameterSerializer,ParameterDetailSerializer


class ParameterViewSet(viewsets.ModelViewSet):
	queryset = Parameter.objects.all()
	serializer_class = ParameterSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title', 'description','category1','category2','status')
	filter_fields = ('name','title','description','category1','category2','status')
	# lookup_field = 'slug'

	# @detail_route()
	# def items(self, request, pk=None):
	# 	parameter = self.get_object()
	# 	serializer = ParameterDetailSerializer(parameter.details.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)
