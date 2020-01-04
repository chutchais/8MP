from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from performing.models import Performing
from performing.api.serializers import PerformingSerializer



class PerformingViewSet(viewsets.ModelViewSet):
	queryset = Performing.objects.all()
	serializer_class = PerformingSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('=sn__number','operation__name','resource_name','result','remark')
	filter_fields = ('sn__number','operation__name','resource_name','result','remark')

	# @detail_route()
	# def users(self, request, pk=None):
	# 	operation = self.get_object()
	# 	serializer = UserAccessListSerializer(operation.users.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)