from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from snippet.models import Snippet
from snippet.api.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','category1','category2', 'description','status')
	filter_fields = ('name','title','category1','category2', 'description','status')
	lookup_field = 'slug'
	# @detail_route()
	# def workorders(self, request, pk=None):
	# 	product = self.get_object()
	# 	serializer = WorkorderSerializer(product.workorders.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)