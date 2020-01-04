from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from defect.models import DefectCode,Defect
from defect.api.serializers import DefectCodeSerializer,DefectSerializer



class DefectViewSet(viewsets.ModelViewSet):
	queryset = Defect.objects.all()
	serializer_class = DefectSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('defectcode')
	filter_fields = ('defectcode','note')

class DefectCodeViewSet(viewsets.ModelViewSet):
	queryset = DefectCode.objects.all()
	serializer_class = DefectCodeSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','description',
				'category1','category2')
	filter_fields = ('name','title','description',
				'category1','category2','status')

