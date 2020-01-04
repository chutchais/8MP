from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from bom.models import Bom,Bom_Detail,Alternate_Part
from bom.api.serializers import BomSerializer,BomDetailSerializer,BomAlternateSerializer


class BomViewSet(viewsets.ModelViewSet):
	queryset = Bom.objects.all()
	serializer_class = BomSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','pn','rev','title','description',
				'fg_pn','fg_rev','category1','category2','status')
	filter_fields = ('name','pn','rev','title','description',
				'fg_pn','fg_rev','category1','category2','status')

	@detail_route()
	def items(self, request, pk=None):
		bom = self.get_object()
		serializer = BomDetailSerializer(bom.items.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)

class BomDetailViewSet(viewsets.ModelViewSet):
	queryset = Bom_Detail.objects.all()
	serializer_class = BomDetailSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('rd','pn','bom__name','customer_pn',
		'pn_type','title','slug','description',
		'category1','category2','status')
	filter_fields = ('rd','pn','bom__name','customer_pn',
		'pn_type','title','slug','description',
		'category1','category2','status')

	@detail_route()
	def alternates(self, request, pk=None):
		bom_detail = self.get_object()
		serializer = BomAlternateSerializer(bom_detail.alternates.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)


class BomAlternateViewSet(viewsets.ModelViewSet):
	queryset = Alternate_Part.objects.all()
	serializer_class = BomAlternateSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('pn', 'description','status')
	filter_fields = ('pn', 'description','status')