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

# from operation.models import Operation
# from .serializers import (OperationListSerializer,
# 						OperationCreateSerializer,
# 						OperationDetailSerializer,
# 						OperationUpdateSerializer)



# class OperationListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = OperationListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Operation.objects.all()
# 		name = self.request.GET.get('q')
# 		if name != None :
# 			queryset_list = Operation.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class OperationDetailAPIView(RetrieveAPIView):
# 	queryset= Operation.objects.all()
# 	serializer_class = OperationDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class OperationDeleteAPIView(DestroyAPIView):
# 	queryset= Operation.objects.all()
# 	serializer_class= OperationDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class OperationCreateAPIView(CreateAPIView):
# 	queryset= Operation.objects.all()
# 	serializer_class= OperationCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# # 	def perform_create(self,serializer):
# # 		print ('Voy is %s' % self.kwargs.get('voy'))
# # 		serializer.save()
# class OperationUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Operation.objects.all()
# 	serializer_class=OperationUpdateSerializer
# 	lookup_field='slug'

