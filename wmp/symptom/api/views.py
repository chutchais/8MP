from django.db.models import Q

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveUpdateDestroyAPIView
	)

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

# from .serialize import VoySerializer,VoyDetailSerializer
# from berth.models import Voy

from symptom_code.models import SymptomCode
from .serialize import (SymptomCodeListSerializer,
						SymptomCodeCreateSerializer,
						SymptomCodeDetailSerializer,
						SymptomCodeUpdateSerializer)



class SymptomCodeListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = SymptomCodeListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list = SymptomCode.objects.all()
		name = self.request.GET.get('q')
		if name != None :
			queryset_list = SymptomCode.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class SymptomCodeDetailAPIView(RetrieveAPIView):
	queryset= SymptomCode.objects.all()
	serializer_class = SymptomCodeDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class SymptomCodeDeleteAPIView(DestroyAPIView):
	queryset= SymptomCode.objects.all()
	serializer_class= SymptomCodeDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class SymptomCodeCreateAPIView(CreateAPIView):
	queryset= SymptomCode.objects.all()
	serializer_class= SymptomCodeCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class SymptomCodeUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=SymptomCode.objects.all()
	serializer_class=SymptomCodeUpdateSerializer
	lookup_field='slug'

