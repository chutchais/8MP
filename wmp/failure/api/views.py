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

from failure.models import Failure
from .serialize import (FailureListSerializer,
						FailureCreateSerializer,
						FailureDetailSerializer,
						FailureUpdateSerializer)



class FailureListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = FailureListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['sn']
	def get_queryset(self,*args,**kwargs):
		queryset_list = Failure.objects.all()
		number = self.request.GET.get("number")
		if number != None :
			queryset_list = Failure.objects.filter(
					Q(sn__number__icontains = number))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class FailureDetailAPIView(RetrieveAPIView):
	queryset= Failure.objects.all()
	serializer_class = FailureDetailSerializer
	lookup_field = 'pk'
	# print ("vessel details")

class FailureDeleteAPIView(DestroyAPIView):
	queryset= Failure.objects.all()
	serializer_class= FailureDetailSerializer
	lookup_field='pk'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class FailureCreateAPIView(CreateAPIView):
	queryset= Failure.objects.all()
	serializer_class= FailureCreateSerializer
	# permission_classes = [IsAuthenticated]

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
			
class FailureUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=Failure.objects.all()
	serializer_class=FailureUpdateSerializer
	lookup_field='pk'

