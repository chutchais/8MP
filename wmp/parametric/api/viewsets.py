from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from parametric.models import Parametric
from parametric.api.serializers import ParametricSerializer


class ParametricViewSet(viewsets.ModelViewSet):
	queryset = Parametric.objects.all()
	serializer_class = ParametricSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('performing__sn__number','item__name','value')
	filter_fields = ('performing__sn__number','item__name','value')
