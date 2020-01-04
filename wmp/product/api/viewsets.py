from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Product
from product.api.serializers import ProductSerializer
from workorder.api.serializers import WorkorderSerializer
# from user_profile.api.serializers import ProfileSerializer,UserAccessListSerializer


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','category1','category2', 'description','status')
	filter_fields = ('name','title','category1','category2', 'description','status')
	lookup_field = 'slug'

	@detail_route()
	def workorders(self, request, pk=None):
		product = self.get_object()
		serializer = WorkorderSerializer(product.workorders.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)