from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from operation.models import Operation
from operation.api.serializers import OperationSerializer
from user_profile.api.serializers import ProfileSerializer,UserAccessListSerializer


class OperationViewSet(viewsets.ModelViewSet):
	queryset = Operation.objects.all()
	serializer_class = OperationSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','operation_type','title','description',
				'customer_name','category1','category2')
	filter_fields = ('name','operation_type','title','description',
				'customer_name','category1','category2','status')
	lookup_field = 'slug'

	@detail_route()
	def users(self, request, pk=None):
		operation = self.get_object()
		serializer = UserAccessListSerializer(operation.users.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)