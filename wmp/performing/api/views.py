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

# from performing.models import Performing
# from .serialize import (PerformingListSerializer,
# 						PerformingCreateSerializer,
# 						PerformingDetailSerializer,
# 						PerformingUpdateSerializer)



# class PerformingListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = PerformingListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['sn']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Performing.objects.all()
# 		number = self.request.GET.get("number")
# 		if number != None :
# 			queryset_list = Performing.objects.filter(
# 					Q(sn__number__icontains = number))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class PerformingDetailAPIView(RetrieveAPIView):
# 	queryset= Performing.objects.all()
# 	serializer_class = PerformingDetailSerializer
# 	lookup_field = 'pk'
# 	# print ("vessel details")

# class PerformingDeleteAPIView(DestroyAPIView):
# 	queryset= Performing.objects.all()
# 	serializer_class= PerformingDetailSerializer
# 	lookup_field='pk'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class PerformingCreateAPIView(CreateAPIView):
# 	queryset= Performing.objects.all()
# 	serializer_class= PerformingCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		serializer.save(user=self.request.user)


# class PerformingUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Performing.objects.all()
# 	serializer_class=PerformingUpdateSerializer
# 	lookup_field='pk'

