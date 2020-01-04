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


# from routing.models import Routing
# from .serialize import (RoutingListSerializer,
# 						RoutingCreateSerializer,
# 						RoutingDetailSerializer,
# 						RoutingUpdateSerializer)



# class RoutingListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = RoutingListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Routing.objects.all()
# 		name = self.request.GET.get('q')
# 		if name != None :
# 			queryset_list = Routing.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class RoutingDetailAPIView(RetrieveAPIView):
# 	queryset= Routing.objects.all()
# 	serializer_class = RoutingDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class RoutingDeleteAPIView(DestroyAPIView):
# 	queryset= Routing.objects.all()
# 	serializer_class= RoutingDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class RoutingCreateAPIView(CreateAPIView):
# 	queryset= Routing.objects.all()
# 	serializer_class= RoutingCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# # 	def perform_create(self,serializer):
# # 		print ('Voy is %s' % self.kwargs.get('voy'))
# # 		serializer.save()
# class RoutingUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Routing.objects.all()
# 	serializer_class=RoutingUpdateSerializer
# 	lookup_field='slug'

