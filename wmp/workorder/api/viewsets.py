from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from workorder.models import WorkOrder
from workorder.api.serializers import WorkorderSerializer
# from user_profile.api.serializers import ProfileSerializer,UserAccessListSerializer


class WorkorderViewSet(viewsets.ModelViewSet):
	queryset = WorkOrder.objects.all()
	serializer_class = WorkorderSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','product__slug','product__name','routing__name','qty','category1','category2', 'description','status')
	filter_fields = ('name','title','product__name','routing__name','qty','category1','category2', 'description','status')
	lookup_field = 'slug'
	# @detail_route()
	# def users(self, request, pk=None):
	# 	operation = self.get_object()
	# 	serializer = UserAccessListSerializer(operation.users.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)