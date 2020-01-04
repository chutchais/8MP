from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from symptom.models import Symptom,SymptomCode
from symptom.api.serializers import SymptomSerializer,SymptomCodeSerializer



class SymptomViewSet(viewsets.ModelViewSet):
	queryset = Symptom.objects.all()
	serializer_class = SymptomSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('symptomcode')
	filter_fields = ('symptomcode','note')

class SymptomCodeViewSet(viewsets.ModelViewSet):
	queryset = SymptomCode.objects.all()
	serializer_class = SymptomCodeSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('name','title','description',
				'category1','category2')
	filter_fields = ('name','title','description',
				'category1','category2','status')

