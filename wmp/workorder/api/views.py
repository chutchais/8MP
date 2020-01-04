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

# from workorder.models import WorkOrder
# from .serialize import (WorkOrderListSerializer,
# 						WorkOrderCreateSerializer,
# 						WorkOrderDetailSerializer,
# 						WorkOrderUpdateSerializer)



# class WorkOrderListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = WorkOrderListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = WorkOrder.objects.all()
# 		name = self.request.GET.get('q')
# 		if name != None :
# 			queryset_list = WorkOrder.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class WorkOrderDetailAPIView(RetrieveAPIView):
# 	queryset= WorkOrder.objects.all()
# 	serializer_class = WorkOrderDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class WorkOrderDeleteAPIView(DestroyAPIView):
# 	queryset= WorkOrder.objects.all()
# 	serializer_class= WorkOrderDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class WorkOrderCreateAPIView(CreateAPIView):
# 	queryset= WorkOrder.objects.all()
# 	serializer_class= WorkOrderCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# # 	def perform_create(self,serializer):
# # 		print ('Voy is %s' % self.kwargs.get('voy'))
# # 		serializer.save()
# class WorkOrderUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=WorkOrder.objects.all()
# 	serializer_class=WorkOrderUpdateSerializer
# 	lookup_field='slug'

