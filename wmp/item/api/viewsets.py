from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from item.models import Item,ItemList
from item.api.serializers import ItemSerializer,ItemListSerializer
from parameter.api.serializers import ParameterSerializer


class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','category1','category2','description','status')
	filter_fields = ('name','title','category1','category2','description','status')
	lookup_field = 'slug'

	@detail_route()
	def lists(self, request, pk=None):
		item = self.get_object()
		serializer = ItemListSerializer(item.lists.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)
	


class ItemListViewSet(viewsets.ModelViewSet):
	queryset = ItemList.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name', 'description','status')
	filter_fields = ('name', 'description','status')
	# lookup_field = 'slug'