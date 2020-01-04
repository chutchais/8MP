# from django.db.models import Q

# from rest_framework.generics import (
# 	CreateAPIView,
# 	DestroyAPIView,
# 	ListAPIView,
# 	UpdateAPIView,
# 	RetrieveAPIView,
# 	RetrieveUpdateAPIView,
# 	RetrieveUpdateDestroyAPIView
# 	)

# from rest_framework.filters import (
# 	SearchFilter,
# 	OrderingFilter,
# 	)

# from rest_framework.permissions import (
# 	AllowAny,
# 	IsAuthenticated,
# 	IsAdminUser,
# 	IsAuthenticatedOrReadOnly,
# 	)

# # from .serialize import VoySerializer,VoyDetailSerializer
# # from berth.models import Voy

# from serialnumber.models import SerialNumber
# from .serialize import (SerialNumberListSerializer,
# 						SerialNumberCreateSerializer,
# 						SerialNumberDetailSerializer,
# 						SerialNumberUpdateSerializer)



# class SerialNumberListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = SerialNumberListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		# wip = self.request.GET.get("wip")
# 		# if wip=='yes':
# 		# 	queryset_list =SerialNumber.objects.filter(wip=True)
# 		# else:
# 		# 	queryset_list =SerialNumber.objects.all()
# 		queryset_list =SerialNumber.objects.all()
# 		q = self.request.GET.get("q")
# 		if q != None :
# 				queryset_list = SerialNumber.objects.filter(
# 					Q(number = q))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class SerialNumberDetailAPIView(RetrieveAPIView):
# 	queryset= SerialNumber.objects.all()
# 	serializer_class = SerialNumberDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class SerialNumberDeleteAPIView(DestroyAPIView):
# 	queryset= SerialNumber.objects.all()
# 	serializer_class= SerialNumberDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class SerialNumberCreateAPIView(CreateAPIView):
# 	queryset= SerialNumber.objects.all()
# 	serializer_class= SerialNumberCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		from django.utils import timezone
# 		now = timezone.now()
# 		serializer.save(user=self.request.user,
# 			last_modified_date=now)

# class SerialNumberUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=SerialNumber.objects.all()
# 	serializer_class=SerialNumberUpdateSerializer
# 	lookup_field='slug'
# 	def perform_update(self,serializer):
# 		from django.utils import timezone
# 		now = timezone.now()
# 		serializer.save(last_modified_date=now)

