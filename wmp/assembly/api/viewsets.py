from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from assembly.models import Assembly,Assembly_Detail,Assembly_Usage
from assembly.api.serializers import AssemblySerializer,AssemblyDetailSerializer,AssemblyUsageSerializer


class AssemblyViewSet(viewsets.ModelViewSet):
	queryset = Assembly.objects.all()
	serializer_class = AssemblySerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','product','title','description',
				'category1','category2','status')
	filter_fields = ('name','product','title','description',
				'category1','category2','status')

	@detail_route()
	def items(self, request, pk=None):
		assembly = self.get_object()
		serializer = AssemblyDetailSerializer(assembly.assembly_details.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)

class AssemblyDetailViewSet(viewsets.ModelViewSet):
	queryset = Assembly_Detail.objects.all()
	serializer_class = AssemblyDetailSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('ordered','assembly__name','part',
		'title','slug','description',
		'category1','category2','status')
	filter_fields = ('ordered','assembly__name','part',
		'title','slug','description',
		'category1','category2','status')

class AssemblyUsageViewSet(viewsets.ModelViewSet):
	queryset = Assembly_Usage.objects.all()
	serializer_class = AssemblyUsageSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('ordered','assembly','routingdetail',
		'title','description',
		'category1','category2','status')
	filter_fields = ('ordered','assembly','routingdetail',
		'title','description',
		'category1','category2','status')
	lookup_field = 'slug'